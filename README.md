# Utsuho

[![CI](https://github.com/juno-rmks/utsuho/actions/workflows/ci.yaml/badge.svg)](https://github.com/juno-rmks/utsuho/actions/workflows/ci.yaml)
[![PyPI version](https://img.shields.io/pypi/v/utsuho.svg)](https://pypi.org/project/utsuho/)
[![Python versions](https://img.shields.io/pypi/pyversions/utsuho.svg)](https://pypi.org/project/utsuho/)
[![License](https://img.shields.io/github/license/juno-rmks/utsuho.svg)](LICENSE)

Utsuho is a Python library for deterministic normalization of Japanese text variants.

It focuses on character-level conversions such as width normalization and kana conversion, while avoiding unrelated transformations that general-purpose Unicode normalization may introduce.

- Bidirectional conversion between half-width and full-width katakana
- Bidirectional conversion between hiragana and katakana
- Configurable handling of spaces, punctuation, ASCII symbols, digits, and alphabets
- Command-line interface for interactive use, scripting, and piped stdin processing
- Model Context Protocol (MCP) server support for tool-based integrations

## Why Utsuho?

Japanese text often mixes multiple representations of the same content, such as half-width and full-width katakana, or hiragana and katakana. Python's Unicode normalization can help in some cases, but it may also perform conversions you do not want, such as changing ASCII symbols or decomposing composite characters.

Utsuho provides explicit, deterministic character-level conversions for these Japanese text variants, making it easier to normalize Japanese text without introducing unrelated transformations.

## Performance

Utsuho is implemented in pure Python, but still provides practical throughput for character-level normalization workloads.

In the project's long-input benchmarks on CPython 3.10, kana conversion is roughly in the 7 to 8 million input characters per second range, while width conversion is roughly in the 1 to 3 million input characters per second range.

These numbers are intended as indicative throughput rather than fixed guarantees, and will vary by platform, Python version, input mix, and power or thermal conditions.

## Installation

Install Utsuho with `pip`:

```sh
pip install Utsuho
```

## Quick Start

### Half-width to full-width katakana

```python
from utsuho import HalfToFullConverter

text = "ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2"
converted = HalfToFullConverter().convert(text)

print(converted)
# キョウトシ　サキョウク　ギンカクジチョウ　２
```

### Full-width to half-width katakana

```python
from utsuho import FullToHalfConverter

text = "キョウトシ　サキョウク　ギンカクジチョウ　２"
converted = FullToHalfConverter().convert(text)

print(converted)
# ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2
```

### Hiragana to katakana

```python
from utsuho import HiraganaToKatakanaConverter

text = "きょうとし　さきょうく　ぎんかくじちょう　２"
converted = HiraganaToKatakanaConverter().convert(text)

print(converted)
# キョウトシ　サキョウク　ギンカクジチョウ　２
```

### Katakana to hiragana

```python
from utsuho import KatakanaToHiraganaConverter

text = "キョウトシ　サキョウク　ギンカクジチョウ　２"
converted = KatakanaToHiraganaConverter().convert(text)

print(converted)
# きょうとし　さきょうく　ぎんかくじちょう　２
```

## Configuring Width Conversion

Use `WidthConverterConfig` to control which non-katakana characters are normalized during half-width and full-width conversion.

```python
from utsuho import HalfToFullConverter, WidthConverterConfig

config = WidthConverterConfig(
    ascii_symbol=False,
    ascii_digit=False,
    ascii_alphabet=False,
)

converted = HalfToFullConverter(config).convert("ｷﾞﾝｶｸｼﾞ 2F")
```

Available options:

| Parameter          | Default | Description                                                                     |
| ------------------ | ------- | ------------------------------------------------------------------------------- |
| `punctuation`      | `True`  | Convert punctuation marks.                                                      |
| `corner_brucket`   | `True`  | Convert corner brackets.                                                        |
| `conjunction_mark` | `True`  | Convert conjunction marks.                                                      |
| `length_mark`      | `True`  | Convert length marks.                                                           |
| `space`            | `True`  | Convert spaces.                                                                 |
| `ascii_symbol`     | `True`  | Convert ASCII symbols.                                                          |
| `ascii_digit`      | `True`  | Convert ASCII digits.                                                           |
| `ascii_alphabet`   | `True`  | Convert ASCII alphabets.                                                        |
| `wave_dash`        | `False` | Convert full-width wave dashes to half-width tildes in full-to-half conversion. |

> [!NOTE]
> The current public API uses the parameter name `corner_brucket` (due to historical reasons).

## CLI

Utsuho also provides a command-line interface for interactive use, scripting, and shell pipelines.

```console
% utsuho --help
Usage: utsuho [OPTIONS] COMMAND [ARGS]...

  Utsuho provides deterministic normalization utilities for Japanese text,
  including width normalization and hiragana/katakana conversion.

Options:
  --version  Show the version.
  --help     Show this message and exit.

Commands:
  full-to-half          Convert from full-width to half-width characters.
  half-to-full          Convert from half-width to full-width characters.
  hiragana-to-katakana  Convert from hiragana to katakana.
  katakana-to-hiragana  Convert from katakana to hiragana.
```

Examples:

```console
% utsuho full-to-half "キョウトシ　サキョウク　ギンカクジチョウ　２"
ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2

% utsuho half-to-full "ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2"
キョウトシ　サキョウク　ギンカクジチョウ　２

% utsuho hiragana-to-katakana "きょうとし　さきょうく　ぎんかくじちょう　２"
キョウトシ　サキョウク　ギンカクジチョウ　２

% utsuho katakana-to-hiragana "キョウトシ　サキョウク　ギンカクジチョウ　２"
きょうとし　さきょうく　ぎんかくじちょう　２

% echo "キョウトシ　２" | utsuho full-to-half
ｷｮｳﾄｼ 2
```

Each command accepts either a `TEXT` argument or piped stdin input.
If `TEXT` is omitted, input is read from stdin.

When `--file` (or `-f`) is specified, `TEXT` is required and is treated as a UTF-8 text file path.
In this mode, stdin input is not used.

## MCP (Model Context Protocol)

Utsuho also provides a Model Context Protocol (MCP) server that exposes its text conversion utilities as tools.

This allows Utsuho to be used from MCP-compatible clients such as AI agents, enabling deterministic text normalization as an external tool.

### Installation

Install with the mcp extra:

```sh
pip install "Utsuho[mcp]"
```

### Running the MCP server

Start the server using:

```sh
utsuho-mcp
```

The server runs over stdio and provides the following tools.

### Available tools

- half_to_full

  Convert half-width text to full-width text.

- full_to_half

  Convert full-width text to half-width text.

- hiragana_to_katakana

  Convert hiragana to katakana.

- katakana_to_hiragana

  Convert katakana to hiragana.

All tools accept `text: str` and return the converted string.

The width-conversion tools also accept optional boolean parameters matching `WidthConverterConfig`:

```text
punctuation
corner_brucket
conjunction_mark
length_mark
space
ascii_symbol
ascii_digit
ascii_alphabet
```

In addition, `full_to_half` accepts:

```text
wave_dash
```

## Documentation

- Documentation: https://utsuho.readthedocs.io/
- Source code: https://github.com/juno-rmks/utsuho/
- Issue tracker: https://github.com/juno-rmks/utsuho/issues/

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.
