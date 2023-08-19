# How to contribute to Utsuho

Utsuho is a Python module that provides conversion functions for Japanese characters. 
We assumed the native language of many contributors to be Japanese.
So, there is no problem you to post Issues and Discussions in Japanese.

Utsuho は、日本語の文字変換機能を提供する Python モジュールです。
主な寄稿者の母国語は日本語と想定しています。
そのため、Issue や Discussion を日本語で投稿しても構いません。

## Setup in your local environment

Fork Utsuho to your GitHub account.

Clone your fork locally, replacing `yourname` in the command below with your actual username.

```console
% git clone git@github.com:yourname/utsuho.git
```

Create and activate a Python virtual environment using version 3.7 or later.

```console
% python -m venv .venv
% . .venv/bin/activate
```

Install Utsuho and its development dependencies in editable mode.

```console
% pip install -e .
% pip install -e .[dev]
% pip install -e .[test]
% pip install -e .[docs]
```

## Running the test

Run all test suites except the benchmark test suite with pytest.

```console
% pytest
```

Run pytest using coverage and generate a report.

```console
% coverage run -m pytest
% coverage html
```

Run only the benchmark test suite with pytest.

```console
% pytest --benchmark-only
```

## Updating the API reference

Update the documentation source to match the current source structure.

```console
% sphinx-apidoc -f -T -e -M -o docs/source src
```

## Building and publishing the package

Generate the distribution archive.

```console
% python -m build
```

Upload the distribution archive to Test PyPi.

```console
% python -m twine upload --repository testpypi dist/*
Enter your username: __token__
Enter your password:
```

Upload the distribution archive to PyPi.

```console
% python -m twine upload dist/*
Enter your username: __token__
Enter your password:
```
