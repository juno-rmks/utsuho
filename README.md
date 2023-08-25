# Utsuho

Utsuho is a Python module that facilitates bidirectional conversion between half-width katakana and full-width katakana in Japanese, as well as between hiragana and katakana.

The name "Utsuho" originates from the narrative "Utsuho Monogatari," believed to have been composed during the mid-Heian period. This narrative contains descriptions related to katakana.

Although the Python standard library allows for the normalization of Unicode strings, enabling the conversion of half-width katakana to full-width katakana, this process may involve unnecessary transformations such as decomposing composite characters and converting full-width alphanumeric symbols to half-width. Additionally, direct conversion from full-width katakana to half-width katakana is not supported.

Utsuho provides bidirectional conversion for half-width katakana and full-width katakana, as well as between hiragana and katakana.

> [!NOTE]
> Starting from version 2.0.0, the functionality for bidirectional conversion between hiragana and katakana has been added.

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
