# Utsuho

Utsuho is a Python module that provides interconversion between Japanese half-width katakana and full-width katakana.

Utsuho currently supports conversion of Katakana and its symbols only. Conversion of ASCII characters and space characters will be supported in the next version.

The name Utsuho comes from the long story "Utsuho Monogatari," which is said to have been written in the middle of the Heian period, and contains descriptions of katakana.

## Installing

Install and update using pip:

```sh
pip install Utsuho
```

## Usage

To convert from half-width katakana to full-width katakana, code as follows.

```python
from utsuho import HalfToFullConverter

halfwidth = 'ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2'
cnv = HalfToFullConverter()
fullwidth = cnv.convert(halfwidth)
```

The conversion result of the above example is "`キョウトシ サキョウク ギンカクジチョウ 2`".

To convert from full-width katakana to half-width katakana, code as follows.

```python
from utsuho import FullToHalfConverter

fullwidth = 'キョウトシ　サキョウク　ギンカクジチョウ　２'
cnv = FullToHalfConverter()
halfwidth = cnv.convert(fullwidth)
```

The conversion result of the above example is "`ｷｮｳﾄｼ　ｻｷｮｳｸ　ｷﾞﾝｶｸｼﾞﾁｮｳ　２`".

## License

This project is licensed under the terms of the Apache license 2.0.

See the ["LICENSE"](https://github.com/juno-rmks/utsuho/blob/main/LICENSE) file for license rights and limitations.

## Links

* [Utsuho document](https://utsuho.readthedocs.io/ja/latest/)
