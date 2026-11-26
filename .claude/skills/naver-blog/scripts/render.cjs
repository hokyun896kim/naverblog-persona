#!/usr/bin/env node
// HTML 파일을 PNG로 뽑는다.
//   node render.cjs <in.html> <out.png> [--w 1080] [--h 1080] [--scale 2]
// --h 를 생략하면 내용 높이에 맞춘다(본문 카드용). --scale 은 해상도 배수(기본 2).
// 한글 글꼴(Pretendard)은 ../assets/fonts 에 들어 있는 파일을 자동으로 끼워 넣는다.
const { chromium } = require('playwright');
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');

const args = process.argv.slice(2);
const pos = [];
const opt = { w: 1080, h: 0, scale: 2 };
for (let i = 0; i < args.length; i++) {
  if (args[i].startsWith('--')) opt[args[i].slice(2)] = Number(args[++i]);
  else pos.push(args[i]);
}
const [input, output] = pos;
if (!input || !output || !fs.existsSync(input) || !(opt.w > 0) || !(opt.scale > 0)) {
  console.error('사용법: node render.cjs <in.html> <out.png> [--w 1080] [--h 1080] [--scale 2]');
  process.exit(1);
}

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: opt.w, height: opt.h || 800 },
    deviceScaleFactor: opt.scale,
  });
  await page.goto(pathToFileURL(path.resolve(input)).href, { waitUntil: 'load' });

  const font = path.join(__dirname, '..', 'assets', 'fonts', 'PretendardVariable.woff2');
  if (fs.existsSync(font)) {
    const b64 = fs.readFileSync(font).toString('base64');
    await page.addStyleTag({
      content: `@font-face{font-family:'Pretendard';font-weight:45 920;font-style:normal;`
        + `src:url(data:font/woff2;base64,${b64}) format('woff2-variations');}`,
    });
  }
  const loaded = await page.evaluate(async () => {
    try { await document.fonts.load("700 40px 'Pretendard'", '가나다'); } catch (e) {}
    await document.fonts.ready;
    return document.fonts.check("700 40px 'Pretendard'", '가나다');
  });
  if (!loaded) console.warn('경고: Pretendard 글꼴을 읽지 못했습니다. 한글이 네모로 나오는지 PNG를 열어 확인하세요.');

  let h = opt.h;
  if (!h) {
    h = await page.evaluate(() => Math.ceil(document.documentElement.getBoundingClientRect().height));
    await page.setViewportSize({ width: opt.w, height: h });
  }
  await page.screenshot({ path: output, clip: { x: 0, y: 0, width: opt.w, height: h } });
  await browser.close();
  console.log(`${output}  ${Math.round(opt.w * opt.scale)}x${Math.round(h * opt.scale)}px`);
})().catch((e) => { console.error(e.message); process.exit(1); });
