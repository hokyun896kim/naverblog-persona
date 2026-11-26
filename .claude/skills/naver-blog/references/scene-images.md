# 구분 그림 — AI 이미지 생성 프롬프트 쓰기

구분 그림은 단락 사이에서 숨을 돌리게 하고, 다음 덩어리가 어떤 장면의 이야기인지 한눈에 알려 주는 그림이다. 정보를 전하지 않는다. 정보는 글이 전한다. 잘 쓴 문단에 도표를 붙이면 같은 말을 두 번 하게 되지만, 그 문단의 장면을 그린 그림 한 장은 글을 읽기 편하게 만든다.

이미지는 직접 만들지 않는다. 운영자가 원하는 생성 도구에 넣을 **프롬프트를 써서 전달**한다. 운영자가 "이미지도 만들어 줘"라고 따로 말했을 때만 연결된 생성 도구를 쓴다. 생성에는 운영자의 크레딧이 든다.

## 무엇을 그릴까

그 덩어리를 읽는 사람이 **그 문제를 실제로 만나는 순간의 장면**을 그린다. 글에서 단서를 가져온다. 언제(연말, 월급날, 고지서가 오는 주), 어디서(식탁, 은행 창구, 출근길 지하철), 무엇을 앞에 두고(고지서, 통장, 달력, 휴대폰, 영수증).

- 주인공은 사물 하나다. 그 덩어리의 열쇠가 되는 물건을 고른다. 날짜 이야기면 달력, 고지서 이야기면 고지서.
- 배경은 한두 가지만 둔다. 화면에 놓이는 것이 다섯을 넘지 않게 한다.
- 사람이 필요하면 작게, 뒷모습이나 옆모습으로 둔다.
- 한 글 안의 그림들은 이어지는 장면처럼 만든다. 같은 식탁, 같은 사람, 같은 노란 물건이 다음 그림에도 나오면 글 전체가 한 이야기로 묶인다.

그리지 않는 것:

- **뜻을 빗댄 그림.** 계단을 오르는 사람(상승), 저울(비교), 전구(아이디어), 돼지 저금통, 악수, 과녁, 물음표, 로봇, 돋보기. AI가 만든 글에 가장 흔히 붙는 그림이라 한눈에 티가 난다. 빗대지 말고 실제 장면을 그린다.
- **글자와 숫자.** 생성 모델은 한글을 깨뜨린다. 고지서나 화면 속 내용은 빈 줄과 네모로 그리게 한다.
- **도표, 그래프, 화살표가 오르내리는 차트.** 가짜 데이터가 된다. 숫자를 보여 줘야 하면 설명 그림(카드)을 쓴다.
- **사실로 오해될 것.** 실존 인물, 특정 회사 간판과 로고, 실제 건물, 앱 화면 캡처처럼 보이는 것.
- **겁주는 그림.** 불타는 차트, 머리를 감싼 사람, 무너지는 건물. 본문에서 겁주지 않는 것과 같은 이유다.

## 고정 스타일

모든 글의 구분 그림은 같은 풍이어야 한다. 풍이 글마다 바뀌면 블로그의 얼굴이 생기지 않고, 풍을 정해 두지 않으면 생성 모델의 기본값(매끈한 입체감, 보라색 그라데이션, 사진 같은 질감)이 나와 AI 티가 난다.

아래 문단을 **모든 프롬프트 끝에 그대로 붙인다.** 고쳐 쓰지 않는다. 색은 썸네일·카드 틀과 같은 색이다.

```
Style: flat editorial illustration with simple geometric shapes and softly rounded corners. Strictly limited palette: deep navy (#14171F), white, light gray (#F3F4F6) and mid gray, with warm yellow (#FFD43B) as the only accent color, used on one object only. Solid flat fills, clean edges, no outlines heavier than a thin line, no gradients, no glow, no drop shadows, no texture, no 3D rendering, no photorealism. Calm, uncluttered composition on a light gray background with generous empty space. Any people are small, simple figures seen from behind or from the side, without facial features. Absolutely no text, letters, numbers, logos, charts, graphs or arrows anywhere in the image. Landscape 3:2 aspect ratio.
```

풍을 바꾸고 싶으면 글마다 바꾸지 말고 이 문단을 한 번 고친다.

## 프롬프트 쓰는 법

프롬프트는 영어로 쓴다. 생성 모델은 대개 영어 묘사를 가장 안정적으로 따른다. 운영자가 무엇을 그리는지 알 수 있게 한국어 한 줄을 함께 적는다.

장면은 두세 문장으로 구체적으로 쓴다. 생성 모델은 이 글을 읽지 않았으므로 "금리 인상의 부담을 표현" 같은 뜻은 전해지지 않는다. 눈에 보이는 것만 쓴다.

1. 무엇이 어디에 놓여 있는가 (주인공 사물과 배경 한두 가지)
2. 어디서 본 모습인가 (위에서 내려다본, 옆에서 본, 조금 떨어져서 본)
3. 노란색을 어디에 쓰는가 (주인공 사물 한 곳)
4. 빈 자리가 어디인가 (필요하면)

종이나 화면이 나오면 "with blank lines instead of text"처럼 내용을 비우라고 적는다. 한국 생활의 장면이면 그 단서를 넣는다(a Korean apartment kitchen, a subway car).

전달할 때의 형식:

```
[이미지 3 — 구분 그림] 소제목 「…」 바로 아래
그리는 것: (한국어 한 줄)
프롬프트:
(장면 두세 문장, 영어) + (고정 스타일 문단)
```

모양을 보여 주는 예 둘 (장면을 가져다 쓰지 않는다):

```
그리는 것: 식탁 위에 펼쳐 놓은 전기요금 고지서와 그 옆의 계산기
프롬프트:
A paper utility bill lying open on a kitchen table in a Korean apartment, seen from directly above. Next to it sit a small calculator and a cup. The bill shows only blank lines and empty boxes instead of text, and its top edge is highlighted in yellow. The right third of the image is left empty.
Style: (고정 스타일 문단)
```

```
그리는 것: 4월 달력의 한 날짜에 표시가 되어 있고, 그 앞에 월급 명세서 봉투가 놓인 책상
프롬프트:
A wall calendar seen straight on, with one date square filled in yellow and all other squares blank. Below it, on a desk, lies a closed envelope and a pen. A small figure seen from behind stands at the left edge looking at the calendar.
Style: (고정 스타일 문단)
```

## 내보내기 전에 보는 것

프롬프트마다 다음을 확인한다.

- 이 그림이 붙는 덩어리의 실제 장면인가, 뜻을 빗댄 그림인가.
- 눈에 보이는 것만 썼는가. 추상적인 말("부담", "불확실성", "성장")이 들어가 있지 않은가.
- 글자, 숫자, 도표를 그리게 하는 말이 없는가.
- 고정 스타일 문단이 그대로 붙어 있는가.
- 같은 글의 다른 그림과 장면이 겹치지 않으면서 이어지는가.

운영자에게는 "올리기 전 확인"에 한 줄을 남긴다. 생성된 그림에 깨진 글자가 들어갔거나, 손·얼굴이 어색하거나, 색이 블로그 색과 다르면 다시 뽑아 달라는 것. 그림은 `02_scene.png`처럼 본문 자리 번호에 맞춰 저장해 달라고 적는다.

이 프롬프트는 2026-11-26 기준으로 실제 생성 도구에 넣어 확인하지 못했다. 운영자가 써 보고 알려 주는 결과로 고정 스타일 문단을 다듬는다.
