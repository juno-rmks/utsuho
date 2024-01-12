# Utsuho

Utsuho is a Python module that facilitates bidirectional conversion between half-width katakana and full-width katakana in Japanese. Furthermore, it offers bidirectional conversion between hiragana and katakana.

> [!NOTE]
> From version 2.0.0 onward, you can now perform bidirectional conversion between hiragana and katakana.

## Background and Goals

In the Japanese character set, both half-width and full-width characters exist. In Japanese, the same data can be represented in either half-width or full-width characters. However, there is no standard for data representation in either half-width or full-width characters. When using Japanese data, you may often encounter inconsistencies between half-width and full-width characters.

In the Python standard library, Unicode string normalization enables the conversion from half-width katakana to full-width katakana. However, this process may involve unnecessary transformations, such as decomposing composite characters and converting full-width alphanumeric symbols to half-width. Furthermore, there is no support for the reverse conversion from full-width katakana to half-width katakana.

Utsuho supports bidirectional conversion between half-width and full-width katakana in Japanese without unnecessary transformations. Additionally, by providing a means to unify various Japanese representations, Utsuho aims to enhance the utility of Japanese data.

## Origin of the Name "Utsuho"

The name "Utsuho" originates from "Utsuho Monogatari," believed to have been composed during the Heian period. This narrative includes descriptions related to learning katakana.

## Installing

Install and update using pip:

```sh
pip install Utsuho
```

## Usage

Using Utsuho, you can perform bidirectional conversion between half-width and full-width characters, as well as between hiragana and katakana.

### Conversion from Half-Width to Full-Width Characters

To convert from half-width to full-width characters, use the following code:

```python
from utsuho import HalfToFullConverter

halfwidth = 'ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2'
cnv = HalfToFullConverter()
fullwidth = cnv.convert(halfwidth)
```

In the above example, the variable `fullwidth` will store the conversion result as "`キョウトシ　サキョウク　ギンカクジチョウ　２`".

### Conversion from Full-Width to Half-Width Characters

To convert from full-width to half-width characters, use the following code:

```python
from utsuho import FullToHalfConverter

fullwidth = 'キョウトシ　サキョウク　ギンカクジチョウ　２'
cnv = FullToHalfConverter()
halfwidth = cnv.convert(fullwidth)
```

In the above example, the variable `halfwidth` will store the conversion result as "`ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2`".

### Conversion from Hiragana to Katakana

To convert from hiragana to katakana, use the following code:

```python
from utsuho import HiraganaToKatakanaConverter

hiragana = 'きょうとし　さきょうく　ぎんかくじちょう　２'
cnv = HiraganaToKatakanaConverter()
katakana = cnv.convert(hiragana)
```

In the above example, the variable `katakana` will store the conversion result as "`キョウトシ　サキョウク　ギンカクジチョウ　２`".

### Conversion from Katakana to Hiragana

To convert from katakana to hiragana, use the following code:

```python
from utsuho import KatakanaToHiraganaConverter

katakana = 'キョウトシ　サキョウク　ギンカクジチョウ　２'
cnv = KatakanaToHiraganaConverter()
hiragana = cnv.convert(katakana)
```

In the above example, the variable `hiragana` will store the coversion result as "`きょうとし　さきょうく　ぎんかくじちょう　２`".

### Configuration of Conversion Behaviors Between Half-Width and Full-Width Characters

The conversion behaviors can be configured by passing an instance of the `WidthConverterConfig` class as an argument to the constructors of either the `HalfToFullConverter` class or the `FullToHalfConverter` class.

> [!NOTE]
> From version 2.0.0 onward, you must use `WidthConverterConfig` instead of `ConverterConfig`.

```python
from utsuho import WidthConverterConfig, HalfToFullConverter

conf = WidthConverterConfig(
  ascii_symbol=False,   # Disable conversion of ASCII symbols
  ascii_digit=False,    # Disable conversion of ASCII digits
  ascii_alphabet=False, # Disable conversion of ASCII alphabets
)
cnv = HalfToFullConverter(conf)
```

The conversion behaviors that can be configured with the `WidthConverterConfig` class are as follows:

| Parameter        | Default Value | Description                           |
| ---------------- | ------------- | ------------------------------------- |
| punctuation      | True          | Whether to convert punctuations.      |
| corner_bracket   | True          | Whether to convert corner brackets.   |
| conjunction_mark | True          | Whether to convert conjunction marks. |
| length_mark      | True          | Whether to convert length marks.      |
| space            | True          | Whether to convert spaces.            |
| ascii_symbol     | True          | Whether to convert ASCII symbols.     |
| ascii_digit      | True          | Whether to convert digits.            |
| ascii_alphabet   | True          | Whether to convert alphabets.         |
| wave_dash        | False         | Whether to convert wave dashes.       |

## License

This project is licensed under the terms of the Apache license 2.0.

See the ["LICENSE"](https://github.com/juno-rmks/utsuho/blob/main/LICENSE) file for license rights and limitations.

## Links

* [Utsuho document](https://utsuho.readthedocs.io/ja/latest/)
