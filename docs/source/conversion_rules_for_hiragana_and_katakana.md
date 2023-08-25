# ひらがなとカタカナの変換規則

ひらがなとカタカナの変換規則を説明します。

## ひらがなからカタカナへの変換規則

Unicode 標準の ["Hiragana"](https://unicode.org/charts/PDF/U3040.pdf) チャートで定義されているひらがなを対応するカタカナへ変換します。

- "Hiragana" チャート
  - "Hiragana letters" (0x3041-0x3094)
  - "Small letters" (0x3095-0x3096)
  - "Iteration marks" (0x309D-0x309E)

ひらがなとカタカナで共用の "Voicing marks" として定義されている濁点と半濁点は変換しません。

対応するカタカナがない "Hiragana digraph" として定義されている合略仮名の "ゟ" (より) は変換しません。

## カタカナからひらがなへの変換規則

Unicode 標準の ["Katakana"](https://www.unicode.org/charts/PDF/U30A0.pdf) チャートで定義されているカタカナを対応するひらがなへ変換します。

- "Katakana" チャート
  - "Katakana letters" (0x30A1-0x30F6)
  - "Iteration marks" (0x30FD-0x30FE)

対応する非合成文字のひらがなのない "Katakana letters" として定義されている "ヷ"、"ヸ"、"ヹ" と "ヺ" は、変換しません。

ひらがなとカタカナで共用の "Conjunction and length marks" として定義されている中黒と長音記号は変換しません。

対応するひらがながない "Katakana digraph" として定義されている合略仮名に類する "ヿ" (コト) は変換しません。

## ひらがなとカタカナのマップ

ひらがなとカタカナのマッピングを示します。

### 清音

| ひらがな    | カタカナ    |
| ----------- | ----------- |
| あ (0x3042) | ア (0x30A2) |
| い (0x3044) | イ (0x30A4) |
| う (0x3046) | ウ (0x30A6) |
| え (0x3048) | エ (0x30A8) |
| お (0x304A) | オ (0x30AA) |
| か (0x304B) | カ (0x30AB) |
| き (0x304D) | キ (0x30AD) |
| く (0x304F) | ク (0x30AF) |
| け (0x3051) | ケ (0x30B1) |
| こ (0x3053) | コ (0x30B3) |
| さ (0x3055) | サ (0x30B5) |
| し (0x3057) | シ (0x30B7) |
| す (0x3059) | ス (0x30B9) |
| せ (0x305B) | セ (0x30BB) |
| そ (0x305D) | ソ (0x30BD) |
| た (0x305F) | タ (0x30BF) |
| ち (0x3061) | チ (0x30C1) |
| つ (0x3064) | ツ (0x30C4) |
| て (0x3066) | テ (0x30C6) |
| と (0x3068) | ト (0x30C8) |
| な (0x306A) | ナ (0x30CA) |
| に (0x306B) | ニ (0x30CB) |
| ぬ (0x306C) | ヌ (0x30CC) |
| ね (0x306D) | ネ (0x30CD) |
| の (0x306E) | ノ (0x30CE) |
| は (0x306F) | ハ (0x30CF) |
| ひ (0x3072) | ヒ (0x30D2) |
| ふ (0x3075) | フ (0x30D5) |
| へ (0x3078) | ヘ (0x30D8) |
| ほ (0x307B) | ホ (0x30DB) |
| ま (0x307E) | マ (0x30DE) |
| み (0x307F) | ミ (0x30DF) |
| む (0x3080) | ム (0x30E0) |
| め (0x3081) | メ (0x30E1) |
| も (0x3082) | モ (0x30E2) |
| や (0x3084) | ヤ (0x30E4) |
| ゆ (0x3086) | ユ (0x30E6) |
| よ (0x3088) | ヨ (0x30E8) |
| ら (0x3089) | ラ (0x30E9) |
| り (0x308A) | リ (0x30EA) |
| る (0x308B) | ル (0x30EB) |
| れ (0x308C) | レ (0x30EC) |
| ろ (0x308D) | ロ (0x30ED) |
| わ (0x308F) | ワ (0x30EF) |
| ゐ (0x3090) | ヰ (0x30F0) |
| ゑ (0x3091) | ヱ (0x30F1) |
| を (0x3092) | ヲ (0x30F2) |
| ん (0x3093) | ン (0x30F3) |

### 小文字

| ひらがな    | カタカナ    |
| ----------- | ----------- |
| ぁ (0x3041) | ァ (0x30A1) |
| ぃ (0x3043) | ィ (0x30A3) |
| ぅ (0x3045) | ゥ (0x30A5) |
| ぇ (0x3047) | ェ (0x30A7) |
| ぉ (0x3049) | ォ (0x30A9) |
| ゕ (0x3095) | ヵ (0x30F5) |
| ゖ (0x3096) | ヶ (0x30F6) |
| っ (0x3063) | ッ (0x30C3) |
| ゃ (0x3083) | ャ (0x30E3) |
| ゅ (0x3085) | ュ (0x30E5) |
| ょ (0x3087) | ョ (0x30E7) |
| ゎ (0x308E) | ヮ (0x30EE) |

### 濁音

| ひらがな    | カタカナ    |
| ----------- | ----------- |
| ゔ (0x3094) | ヴ (0x30F4) |
| が (0x304C) | ガ (0x30AC) |
| ぎ (0x304E) | ギ (0x30AE) |
| ぐ (0x3050) | グ (0x30B0) |
| げ (0x3052) | ゲ (0x30B2) |
| ご (0x3054) | ゴ (0x30B4) |
| ざ (0x3056) | ザ (0x30B6) |
| じ (0x3058) | ジ (0x30B8) |
| ず (0x305A) | ズ (0x30BA) |
| ぜ (0x305C) | ゼ (0x30BC) |
| ぞ (0x305E) | ゾ (0x30BE) |
| だ (0x3060) | ダ (0x30C0) |
| ぢ (0x3062) | ヂ (0x30C2) |
| づ (0x3065) | ヅ (0x30C5) |
| で (0x3067) | デ (0x30C7) |
| ど (0x3069) | ド (0x30C9) |
| ば (0x3070) | バ (0x30D0) |
| び (0x3073) | ビ (0x30D3) |
| ぶ (0x3076) | ブ (0x30D6) |
| べ (0x3079) | ベ (0x30D9) |
| ぼ (0x307C) | ボ (0x30DC) |

### 半濁音

| ひらがな    | カタカナ    |
| ----------- | ----------- |
| ぱ (0x3071) | パ (0x30D1) |
| ぴ (0x3074) | ピ (0x30D4) |
| ぷ (0x3077) | プ (0x30D7) |
| ぺ (0x307A) | ペ (0x30DA) |
| ぽ (0x307D) | ポ (0x30DD) |

### 踊り字

| ひらがな    | カタカナ    |
| ----------- | ----------- |
| ゝ (0x309D) | ヽ (0x30FD) |
| ゞ (0x309E) | ヾ (0x30FE) |