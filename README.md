# Utsuho

Utsuho is a Python module that provides interconversion between Japanese half-width katakana and full-width katakana.

The name Utsuho comes from the long story "Utsuho Monogatari," which is said to have been written in the middle of the Heian period, and contains descriptions of katakana.

**Utsuho は、日本語を取り扱う Python モジュールであり、日本語を母語とするユーザーを想定しているため、Issue や Discussion を日本語で投稿いただいて構いません。**

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

The conversion result of the above example is "`キョウトシ　サキョウク　ギンカクジチョウ　２`".

To convert from full-width katakana to half-width katakana, code as follows.

```python
from utsuho import FullToHalfConverter

fullwidth = 'キョウトシ　サキョウク　ギンカクジチョウ　２'
cnv = FullToHalfConverter()
halfwidth = cnv.convert(fullwidth)
```

The conversion result of the above example is "`ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2`".

## License

This project is licensed under the terms of the Apache license 2.0.

See the ["LICENSE"](https://github.com/juno-rmks/utsuho/blob/main/LICENSE) file for license rights and limitations.

## Development

**This is just a note for me.**

Create a Python virtual environment and activate it.

```console
% python -m venv .venv
% . .venv/bin/activate
```

Install Utsuho locally with `--editable` option.

```console
% pip install -e .
% pip install -e .[test]
% pip install -e .[dev]
% pip install -e .[docs]
```

### Update API Reference

Update the documentation source to match the current source structure.

```console
% sphinx-apidoc -f -T -e -M -o docs/source src
```

### Build and Publish Package

Generate the distribution archive.

```console
python -m build
```

Upload the distribution archive to Test PyPi.

```console
python -m twine upload --repository testpypi dist/*
Enter your username: __token__
Enter your password:
```

Upload the distribution archive to PyPi.

```console
python -m twine upload dist/*
Enter your username: __token__
Enter your password:
```

## Links

* [Utsuho document](https://utsuho.readthedocs.io/ja/latest/)
