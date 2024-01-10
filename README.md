# Utsuho

Utsuho is a Python module that facilitates bidirectional conversion between half-width katakana and full-width katakana in Japanese. Furthermore, it offers bidirectional conversion between hiragana and katakana.

> [!NOTE]
> From version 2.0.0 onward, you can now perform bidirectional conversion between hiragana and katakana.

## Background and Goals

In the Japanese character set, both half-width and full-width characters exist. In Japanese, the same data can be represented in either half-width or full-width characters. However, there is no standard for data representation in either half-width or full-width characters. When using Japanese data, you may often encounter inconsistencies between half-width and full-width characters.

In the Python standard library, Unicode string normalization enables the conversion from half-width katakana to full-width katakana. However, this process may involve unnecessary transformations, such as decomposing composite characters and converting full-width alphanumeric symbols to half-width. Furthermore, there is no support for the reverse conversion from full-width katakana to half-width katakana.

Utsuho supports bidirectional conversion between half-width and full-width katakana in Japanese without unnecessary transformations. Additionally, by providing a means to unify various Japanese representations, Utsuho aims to enhance the utility of Japanese data.

## Origin of the name "Utsuho"

The name "Utsuho" originates from "Utsuho Monogatari," believed to have been composed during the Heian period. This narrative includes descriptions related to learning katakana.

## Installing

Install and update using pip:

```sh
pip install Utsuho
```

## Usage

### Conversion from half-width katakana to full-width katakana

To convert from half-width katakana to full-width katakana, code as follows.

```python
from utsuho import HalfToFullConverter

halfwidth = 'ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2'
cnv = HalfToFullConverter()
fullwidth = cnv.convert(halfwidth)
```

The conversion result of the above example is "`キョウトシ　サキョウク　ギンカクジチョウ　２`".

### Conversion from full-width katakana to half-width katakana

To convert from full-width katakana to half-width katakana, code as follows.

```python
from utsuho import FullToHalfConverter

fullwidth = 'キョウトシ　サキョウク　ギンカクジチョウ　２'
cnv = FullToHalfConverter()
halfwidth = cnv.convert(fullwidth)
```

The conversion result of the above example is "`ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2`".

### Conversion from hiragana to katakana

To convert from hiragana to katakana, code as follows.

```python
from utsuho import HiraganaToKatakanaConverter

hiragana = 'きょうとし　さきょうく　ぎんかくじちょう　２'
cnv = HiraganaToKatakanaConverter()
katakana = cnv.convert(hiragana)
```

The conversion result of the above example is "`キョウトシ　サキョウク　ギンカクジチョウ　２`".

### Conversion from katakana to hiragana

To convert from katakana to hiragana, code as follows.

```python
from utsuho import KatakanaToHiraganaConverter

katakana = 'キョウトシ　サキョウク　ギンカクジチョウ　２'
cnv = KatakanaToHiraganaConverter()
hiragana = cnv.convert(katakana)
```

The conversion result of the above example is "`きょうとし　さきょうく　ぎんかくじちょう　２`".

## License

This project is licensed under the terms of the Apache license 2.0.

See the ["LICENSE"](https://github.com/juno-rmks/utsuho/blob/main/LICENSE) file for license rights and limitations.

## Links

* [Utsuho document](https://utsuho.readthedocs.io/ja/latest/)
