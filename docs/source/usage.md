# 使用方法

Utsuho を使用して、半角文字と全角文字の相互変換とひらがなとカタカナの相互変換を実施できます。

## 半角文字から全角文字への変換

半角文字から全角文字への変換には、次のコードを使用します。

```python
from utsuho import HalfToFullConverter

halfwidth = 'ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2'
cnv = HalfToFullConverter()
fullwidth = cnv.convert(halfwidth)
```

上記の例では、`fullwidth` 変数に変換結果として "`キョウトシ　サキョウク　ギンカクジチョウ　２`" が格納されます。

## 全角文字から半角文字への変換

全角文字から半角文字への変換には、次のコードを使用します。

```python
from utsuho import FullToHalfConverter

fullwidth = 'キョウトシ　サキョウク　ギンカクジチョウ　２'
cnv = FullToHalfConverter()
halfwidth = cnv.convert(fullwidth)
```

上記の例では、`halfwidth` 変数に変換結果として "`ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2`" が格納されます。

## ひらがなからカタカナへの変換

ひらがなからカタカナへの変換には、次のコードを使用します。

```python
from utsuho import HiraganaToKatakanaConverter

hiragana = 'きょうとし　さきょうく　ぎんかくじちょう　２'
cnv = HiraganaToKatakanaConverter()
katakana = cnv.convert(hiragana)
```

上記の例では、`katakana` 変数に変換結果として "`キョウトシ　サキョウク　ギンカクジチョウ　２`" が格納されます。

## カタカナからひらがなへの変換

カタカナからひらがなへの変換には、次のコードを使用します。

```python
from utsuho import KatakanaToHiraganaConverter

katakana = 'キョウトシ　サキョウク　ギンカクジチョウ　２'
cnv = KatakanaToHiraganaConverter()
hiragana = cnv.convert(katakana)
```

上記の例では、`hiragana` 変数に変換結果として "`きょうとし　さきょうく　ぎんかくじちょう　２`" が格納されます。

## 半角文字と全角文字間の変換の設定

変換の振る舞いは、`WidthConverterConfig` クラスのインスタンスを `HalfToFullConverter` クラスや `FullToHalfConverter` クラスのコンストラクターの引数へ引き渡すことで設定できます。

:::{note}
バージョン 2.0.0 以降 `ConverterConfig` ではなく `WidthConverterConfig` を使用しなければなりません。
:::

```python
from utsuho import WidthConverterConfig, HalfToFullConverter

conf = WidthConverterConfig(
  ascii_symbol=False,   # ASCII 記号の変換を無効にする
  ascii_digit=False,    # ASCII 数字の変換を無効にする
  ascii_alphabet=False, # ASCII アルファベットの変換を無効にする
)
cnv = HalfToFullConverter(conf)
```

`WidthConverterConfig` クラスで設定できる変換の振る舞いは、次の通りです。

| パラメーター     | デフォルト値 | 説明                                     |
| ---------------- | ------------ | ---------------------------------------- |
| punctuation      | True         | 句読点を変換するかどうか。               |
| corner_brucket   | True         | 鉤括弧を変換するかどうか。               |
| conjunction_mark | True         | 中黒を変換するかどうか。                 |
| length_mark      | True         | 長音記号を変換するかどうか。             |
| space            | True         | スペースを変換するかどうか。             |
| ascii_symbol     | True         | ASCII 記号を変換するかどうか。           |
| ascii_digit      | True         | ASCII 数字を変換するかどうか。           |
| ascii_alphabet   | True         | ASCII アルファベットを変換するかどうか。 |
| wave_dash        | False        | ウェーブダッシュを変換するかどうか。     |
