# 구분 그림 — AI 이미지 생성 프롬프트 쓰기

구분 그림은 단락 사이에서 숨을 돌리게 하고, 다음 덩어리가 어떤 장면의 이야기인지 한눈에 알려 주는 그림이다. 정보를 전하지 않는다. 정보는 글이 전한다. 잘 쓴 문단에 도표를 붙이면 같은 말을 두 번 하게 되지만, 그 문단의 장면을 그린 그림 한 장은 글을 읽기 편하게 만든다.

이미지는 직접 만들지 않는다. 운영자가 원하는 생성 도구에 넣을 **프롬프트를 써서 전달**한다. 운영자가 "이미지도 만들어 줘"라고 따로 말했을 때만 연결된 생성 도구를 쓴다. 생성에는 운영자의 크레딧이 든다.

운영자는 프롬프트마다 생성하고, 확인하고, 마음에 안 들면 다시 뽑고, 저장해야 한다. 한 편에 쓰는 시간이 15분쯤이므로 구분 그림은 **한 글에 두 장을 기본으로 하고 많아야 세 장**이다.

## 무엇을 그릴까

그 덩어리를 읽는 사람이 **그 문제를 실제로 만나는 순간의 장면**을 그린다. 글에서 단서를 가져온다. 언제(연말, 월급날, 고지서가 오는 주), 어디서(식탁, 은행 창구, 출근길 지하철, 우편함 앞), 무엇을 앞에 두고(고지서, 통장, 휴대폰, 영수증, 계약서).

- 주인공은 사물 하나다. 그 덩어리의 열쇠가 되는 물건을 고른다.
- 배경은 한두 가지만 둔다. 화면에 놓이는 것이 다섯을 넘지 않게 한다.
- 사람이 필요하면 작게, 뒷모습이나 옆모습으로 둔다.
- 그림마다 보는 자리를 바꾼다. 한 장이 위에서 내려다본 식탁이면 다음 장은 조금 떨어져서 본 방 안, 그다음은 옆에서 본 창구처럼. 전부 책상 위 물건이면 단조롭다.

독자의 생활 장면이 없는 덩어리도 있다(제도가 돌아가는 방식을 설명하는 덩어리 같은 것). 그럴 때는 그 덩어리에 나오는 실제 장소나 사물을 그린다. 간판 없는 은행 창구, 서류가 쌓인 사무실 책상, 공시가 뜨는 날 아침의 거리. 그것도 마땅치 않으면 자료를 펴 놓고 맞춰 보는 책상을 그릴 수 있지만, 이건 마지막 수단이다. 화면이나 종이 속 내용은 비워 둔다.

한 글 안의 그림들은 이어지는 장면처럼 만든다. 생성 모델은 앞 프롬프트를 기억하지 못하므로, **같은 묘사 구절을 프롬프트마다 그대로 되풀이해서** 잇는다. 같은 사람("a small figure in a navy coat"), 같은 소품("a white mug")을 똑같은 낱말로 적는다. 노란색은 그림마다 그 그림의 주인공 한 곳에만 쓴다. 이어 주는 것은 노란색이 아니라 사람과 소품이다.

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
Style: flat editorial illustration with simple geometric shapes and softly rounded corners. Strictly limited palette: deep navy (#14171F), white, light gray (#F3F4F6) and mid gray, with warm yellow (#FFD43B) as the only accent color, used on one object only. Solid flat fills, clean edges, no outlines heavier than a thin line, no gradients, no glow, no drop shadows, no texture, no 3D rendering, no photorealism. The setting is reduced to a few flat shapes on a plain light gray backdrop rather than a fully drawn room, with generous empty space. Any people are small, simple figures seen from behind or from the side, without facial features. Absolutely no text, letters, numbers, logos, charts, graphs or arrows anywhere in the image. Landscape 3:2 aspect ratio.
```

풍을 바꾸고 싶으면 글마다 바꾸지 말고 이 문단을 한 번 고친다.

## 프롬프트 쓰는 법

프롬프트는 영어로 쓴다. 생성 모델은 대개 영어 묘사를 가장 안정적으로 따른다. 운영자가 무엇을 그리는지 알 수 있게 한국어 한 줄을 함께 적는다.

장면은 두세 문장으로 구체적으로 쓴다. 생성 모델은 이 글을 읽지 않았으므로 "금리 인상의 부담을 표현" 같은 뜻은 전해지지 않는다. 눈에 보이는 것만 쓴다.

1. 무엇이 어디에 놓여 있는가 (주인공 사물과 배경 한두 가지)
2. 어디서 본 모습인가
3. 노란색을 어디에 쓰는가 (주인공 사물 한 곳)

종이나 화면이 나오면 "with blank lines instead of text"처럼 내용을 비우라고 적는다. 한국 생활의 장면이면 그 단서를 넣는다(a Korean apartment hallway, a subway platform).

## 전달 형식

`[이미지 프롬프트]`에는 본문에 들어가는 이미지를 **자리 순서대로 전부** 적는다. 파일로 보내는 것(썸네일, 설명 그림)은 파일 이름만, 구분 그림은 프롬프트까지 적는다. 그래야 운영자가 번호를 건너뛰지 않고 차례로 넣을 수 있다. 프롬프트는 통째로 복사할 수 있게 코드 블록에 넣는다.

````
[이미지 1 — 썸네일] 도입 문단 뒤 · 파일 01_thumb.png

[이미지 2 — 구분 그림] 소제목 「…」 아래 / 또는 「…로 끝나는 문단」 뒤
그리는 것: (한국어 한 줄)
저장할 이름: 02_scene.png
```
(장면 두세 문장, 영어)
Style: (고정 스타일 문단 전체)
```

[이미지 3 — 설명 그림] 「…로 끝나는 문단」 뒤 · 파일 03_table.png
````

장면 문장의 모양을 보여 주는 예 둘 (장면과 구도를 가져다 쓰지 않는다. 글마다 그 글의 장면을 새로 고른다):

```
그리는 것: 아파트 현관 우편함에서 고지서 봉투를 꺼내는 사람의 뒷모습
A small figure in a navy coat, seen from behind, pulls an envelope out of a row of apartment mailboxes in a Korean apartment lobby. The envelope in the figure's hand is yellow; every other mailbox is closed and plain.
```

```
그리는 것: 주유소에서 주유기 앞에 선 차와, 숫자 칸이 비어 있는 가격판
A small car parked beside a fuel pump at a gas station, seen from across the street. A tall price sign stands at the roadside with empty rectangles where the prices would be, and the pump nozzle is yellow.
```

## 내보내기 전에 보는 것

프롬프트마다 다음을 확인한다.

- 이 그림이 붙는 덩어리의 실제 장면인가, 뜻을 빗댄 그림인가.
- 눈에 보이는 것만 썼는가. 추상적인 말("부담", "불확실성", "성장")이 들어가 있지 않은가.
- 글자, 숫자, 도표를 그리게 하는 말이 없는가.
- 고정 스타일 문단이 그대로 붙어 있는가.
- 같은 글의 다른 그림과 보는 자리가 다른가, 사람과 소품은 같은 낱말로 이어지는가.
- 위의 예시와 같은 장면·같은 구도가 아닌가.

운영자에게는 "올리기 전 확인"에 한 줄을 남긴다. 생성된 그림에 깨진 글자가 들어갔거나, 손·얼굴이 어색하거나, 색이 블로그 색과 다르면 다시 뽑아 달라는 것.

이 프롬프트는 2026-11-26 기준으로 실제 생성 도구에 넣어 확인하지 못했다. 운영자가 써 보고 알려 주는 결과로 고정 스타일 문단을 다듬는다.
