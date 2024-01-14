# How to contribute to Utsuho

Thank you for considering contributing to Utsuho!

> [!NOTE]
> We assumed the native language of many contributors to be Japanese.
> So, there is no problem you to post Issues and Discussions in Japanese.
> 
> 主な寄稿者の母国語は日本語と想定しています。
> そのため、Issues や Discussions を日本語で投稿しても構いません。

## Creating a pull request

To activate the project, creating pull requests is highly encouraged. When creating a pull request, please set the destination branch to the `develop` branch.

## Setup in your local environment

Fork Utsuho to your GitHub account.

Clone your fork locally, replacing `yourname` in the command below with your actual username.

```console
% git clone git@github.com:yourname/utsuho.git
```

Create and activate a Python virtual environment using version 3.8 or later.

```console
% python -m venv .venv
% . .venv/bin/activate
```

Install Utsuho and its development dependencies in editable mode.

```console
% pip install --upgrade pip
% pip install -e .
% pip install -e .[dev]
% pip install -e .[test]
% pip install -e .[docs]
```

Note for macOS users:
Escape square brackets with a backslash, e.g., \\[dev\\], when running these commands.

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
% sphinx-apidoc -f -T -e -M -o docs/source/api src
```

## Building and publishing the package

 > [!NOTE]
 > This operation can only be performed by the project owner.

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
