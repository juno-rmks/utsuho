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

## CLI (Command Line Interface)

Utsuho not only serves as a Python library but also provides a straightforward command-line interface that can be used interactively.

### Syntax

You can use the `--help` option to show the CLI syntax.

```console
% utsuho --help
Usage: utsuho [OPTIONS] COMMAND [ARGS]...

  Utsuho is a Python module that facilitates bidirectional conversion between
  half-width katakana and full-width katakana in Japanese. Furthermore, it
  offers bidirectional conversion between hiragana and katakana.

Options:
  --version  Show the version.
  --help     Show this message and exit.

Commands:
  full-to-half          Convert from full-width to half-width characters.
  half-to-full          Convert from half-width to full-width characters.
  hiragana-to-katakana  Convert from hiragana to katakana.
  katakana-to-hiragana  Convert from katakana to hiragana.
```

#### `--version` Option

You can use the `--version` option to display the version of Utsuho. After displaying the version, Utsuho will exit.

If specified along with other options or commands, Utsuho will display its version and exit.

```console
% utsuho --version
Utsuho x.x.x
```

#### Commands

Utsuho provides the following commands:

- `full-to-half` Command

  This command performs the conversion from full-width to half-width characters.

- `half-to-full` Command

  This command performs the conversion from half-width to full-width characters.

- `hiragana-to-katakana` Command

  This command executes the conversion from hiragana to katakana.

- `katakana-to-hiragana` Command

  This command executes the conversion from katakana to hiragana.

### `full-to-half` Command

This command performs the conversion from full-width to half-width characters.

You can use the `--help` option to show the command syntax.

```console
% utsuho full-to-half --help
Usage: utsuho full-to-half [OPTIONS] TEXT

  Convert from full-width to half-width characters.

Options:
  -f, --file  Whether to use TEXT as a file path.
  --help      Show this message and exit.
```

You can convert full-width characters contained in the `TEXT` to half-width characters. The conversion result will be output to the standard output.

```console
% utsuho full-to-half "キョウトシ　サキョウク　ギンカクジチョウ　２"
ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2
```

#### `--file` Option

The `TEXT` parameter is treated as the path to a file that contains the string to be converted.

You can convert full-width characters in the file to half-width characters. The conversion result will be output to the standard output.

Create a file named "full.txt" containing full-width characters.

full.txt:

```text
キョウトシ　サキョウク　ギンカクジチョウ　２
```

Execute the command with the `--file` option and the file path "full.txt":

```console
% utsuho full-to-half --file full.txt
ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2
```

### `half-to-full` Command

This command performs the conversion from half-width to full-width characters.

You can use the `--help` option to show the command syntax.

```console
% utsuho half-to-full --help
Usage: utsuho half-to-full [OPTIONS] TEXT

  Convert from half-width to full-width characters.

Options:
  -f, --file  Whether to use TEXT as a file path.
  --help      Show this message and exit.
```

You can convert half-width characters contained in the `TEXT` to full-width characters. The conversion result will be output to the standard output.

```console
% utsuho half-to-full "ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2"
キョウトシ　サキョウク　ギンカクジチョウ　２
```

#### `--file` Option

The `TEXT` parameter is treated as the path to a file that contains the string to be converted.

You can convert half-width characters in the file to full-width characters. The conversion result will be output to the standard output.

Create a file named "half.txt" containing half-width characters.

half.txt:

```text
ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2
```

Execute the command with the `--file` option and the file path "half.txt":

```console
% utsuho half-to-full --file half.txt
キョウトシ　サキョウク　ギンカクジチョウ　２
```

### `hiragana-to-katakana` Command

This command performs the conversion from hiragana to katakana.

You can use the `--help` option to show the command syntax.

```console
% utsuho hiragana-to-katakana --help
Usage: utsuho hiragana-to-katakana [OPTIONS] TEXT

  Convert from hiragana to katakana.

Options:
  -f, --file  Whether to use TEXT as a file path.
  --help      Show this message and exit.
```

You can convert hiragana contained in the `TEXT` to katakna. The conversion result will be output to the standard output.

```console
% utsuho hiragana-to-katakana "きょうとし　さきょうく　ぎんかくじちょう　２"
キョウトシ　サキョウク　ギンカクジチョウ　２
```

#### `--file` Option

The `TEXT` parameter is treated as the path to a file that contains the string to be converted.

You can convert hiragana in the file to katakana. The conversion result will be output to the standard output.

Create a file named "hiragana.txt" containing hiragana.

hiragana.txt:

```text
きょうとし　さきょうく　ぎんかくじちょう　２
```

Execute the command with the `--file` option and the file path "hiragana.txt":

```console
% utsuho hiragana-to-katakana --file hiragana.txt
キョウトシ　サキョウク　ギンカクジチョウ　２
```

### `katakana-to-hiragana` Command

This command performs the conversion from katakana to hiragana.

You can use the `--help` option to show the command syntax.

```console
% utsuho katakana-to-hiragana --help
Usage: utsuho katakana-to-hiragana [OPTIONS] TEXT

  Convert from katakana to hiragana.

Options:
  -f, --file  Whether to use TEXT as a file path.
  --help      Show this message and exit.
```

You can convert katakana contained in the `TEXT` to hiragana. The conversion result will be output to the standard output.

```console
% utsuho katakana-to-hiragana "キョウトシ　サキョウク　ギンカクジチョウ　２"
きょうとし　さきょうく　ぎんかくじちょう　２
```

#### `--file` Option

The `TEXT` parameter is treated as the path to a file that contains the string to be converted.

You can convert katakana in the file to hiragana. The conversion result will be output to the standard output.

Create a file named "katakana.txt" containing hiragana.

katakana.txt:

```text
キョウトシ　サキョウク　ギンカクジチョウ　２
```

Execute the command with the `--file` option and the file path "katakana.txt":

```console
% utsuho katakana-to-hiragana --file katakana.txt
きょうとし　さきょうく　ぎんかくじちょう　２
```

## License

This project is licensed under the terms of the Apache license 2.0.

See the ["LICENSE"](https://github.com/juno-rmks/utsuho/blob/main/LICENSE) file for license rights and limitations.

## Links

* [Utsuho document](https://utsuho.readthedocs.io/ja/latest/)
