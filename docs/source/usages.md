# 使用方法

使用方法を説明します。

## 半角と全角の相互変換方法

半角と全角の相互変換方法を説明します。

### 半角から全角への変換方法

半角から全角への変換には、[`utsuho.converters.HalfToFullConverter`](#utsuho.converters.HalfToFullConverter) クラスを使用します。

```python
from utsuho import HalfToFullConverter

halfwidth = 'ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2'
cnv = HalfToFullConverter()
fullwidth = cnv.convert(halfwidth)
```

上記の例では、`fullwidth` 変数に変換結果として "`キョウトシ　サキョウク　ギンカクジチョウ　２`" が格納されます。

### 全角から半角への変換方法

全角から半角への変換には、[`utsuho.converters.FullToHalfConverter`](#utsuho.converters.FullToHalfConverter) クラスを使用します。

```python
from utsuho import FullToHalfConverter

fullwidth = 'キョウトシ　サキョウク　ギンカクジチョウ　２'
cnv = FullToHalfConverter()
halfwidth = cnv.convert(fullwidth)
```

上記の例では、`halfwidth` 変数に変換結果として "`ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2`" が格納されます。

### 全角と半角の変換動作の変更方法

:::{note}
バージョン 2.0.0 より `utsuho.converters.ConverterConfig` ではなく `utsuho.converters.WidthConverterConfig` を使用するように変更しました。
:::

変換動作は、各 Converter クラスのコンストラクターの引数へカスタマイズした [`utsuho.converters.WidthConverterConfig`](#utsuho.converters.WidthConverterConfig) クラスのインスタンスを渡すことで変更できます。

```python
from utsuho import WidthConverterConfig, HalfToFullConverter

conf = WidthConverterConfig(punctuation=False)
cnv = HalfToFullConverter(conf)
```

カタカナ文字以外の変換動作は、`utsuho.converters.WidthConverterConfig` クラスの次のパラメーターを設定します。

| パラメーター     | デフォルト値 | 説明                                                   |
| ---------------- | ------------ | ------------------------------------------------------ |
| punctuation      | True         | 句読点を変換するかどうかを切り替えできます。           |
| corner_brucket   | True         | 鉤括弧を変換するかどうかを切り替えできます。           |
| conjunction_mark | True         | 中黒を変換するかどうかを切り替えできます。             |
| length_mark      | True         | 長音記号を変換するかどうかを切り替えできます。         |
| space            | True         | スペースを変換するかどうかを切り替えできます。         |
| ascii_symbol     | True         | 記号を変換するかどうかを切り替えできます。             |
| ascii_digit      | True         | 数字を変換するかどうかを切り替えできます。             |
| ascii_alphabet   | True         | アルファベットを変換するかどうかを切り替えできます。   |
| wave_dash        | True         | ウェーブダッシュを変換するかどうかを切り替えできます。 |

## ひらがなとカタカナの相互変換方法

ひらがなとカタカナの相互変換方法を説明します。

### ひらがなからカタカナへの変換方法

ひらがなからカタカナへの変換には、[`utsuho.converters.HiraganaToKatakanaConverter`](#utsuho.converters.HiraganaToKatakanaConverter) クラスを使用します。

```python
from utsuho import HiraganaToKatakanaConverter

hiragana = 'きょうとし　さきょうく　ぎんかくじちょう　２'
cnv = HiraganaToKatakanaConverter()
katakana = cnv.convert(hiragana)
```

上記の例では、`katakana` 変数に変換結果として "`キョウトシ　サキョウク　ギンカクジチョウ　２`" が格納されます。

### カタカナからひらがなへの変換方法

カタカナからひらがなへの変換には、[`utsuho.converters.KatakanaToHiraganaConverter`](#utsuho.converters.KatakanaToHiraganaConverter) クラスを使用します。

```python
from utsuho import KatakanaToHiraganaConverter

katakana = 'キョウトシ　サキョウク　ギンカクジチョウ　２'
cnv = KatakanaToHiraganaConverter()
hiragana = cnv.convert(katakana)
```

上記の例では、`hiragana` 変数に変換結果として "`きょうとし　さきょうく　ぎんかくじちょう　２`" が格納されます。
