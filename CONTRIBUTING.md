# Contributing to Utsuho

Thank you for your interest in contributing to Utsuho.

> [!NOTE]
> Many contributors are expected to be Japanese speakers.
> You are welcome to open Issues and Discussions in Japanese.
>
> 主な寄稿者の母国語は日本語と想定しています。
> そのため、Issues や Discussions を日本語で投稿しても構いません。

## Pull Requests

Pull requests are welcome.
Please open pull requests against the `main` branch.
Small, focused pull requests are preferred.

For changes that affect behavior, documentation, packaging, or the release workflow, please update the relevant files in the same pull request whenever possible.
If your change affects the CLI, please also update the README examples or help text as needed.

## Local Setup

Fork the repository and clone your fork locally:

```console
% git clone git@github.com:yourname/utsuho.git
% cd utsuho
```

Create and activate a virtual environment with Python 3.10 or later:

```console
% python -m venv .venv
% . .venv/bin/activate
```

Install Utsuho and its development dependencies:

```console
% python -m pip install --upgrade pip
% pip install -e ".[dev]"
```

The first command uses `python -m pip` to make sure `pip` is upgraded for the active interpreter.
On some shells, such as `zsh`, you may need to escape or quote the square brackets in `.[dev]`.

## Running Checks Locally

Run the linter:

```console
% pylint src/utsuho
```

Run the format checks:

```console
% black --check .
% isort --check-only .
```

Run the test suite except benchmarks:

```console
% pytest
```

Run the benchmark suite only:

```console
% pytest --benchmark-only
```

Generate a coverage report:

```console
% coverage run -m pytest
% coverage html
```

## CI

GitHub Actions runs CI automatically for pushes to `main`, pull requests targeting `main`, and manual workflow dispatches.

The CI workflow tests supported Python versions on Ubuntu, macOS, and Windows, and runs lint, format, and test checks.

Please make sure your changes pass the local checks before opening a pull request.

## Documentation Workflow

To refresh the API reference source files:

```console
% sphinx-apidoc -f -T -e -M -o docs/source/api src
```

Documentation is built on Read the Docs using [`.readthedocs.yaml`](.readthedocs.yaml).

## Building Packages Locally

To build source and wheel distributions locally:

```console
% python -m build
```

This is useful for validating packaging changes before pushing a release tag.

## CD and Releases

Release publishing is automated with GitHub Actions.

When a Git tag is pushed:

- the release workflow builds the distribution artifacts
- the artifacts are published to TestPyPI
- the artifacts are also published to PyPI unless the tag name contains `rc`

In other words:

- prerelease tags such as `1.0.0rc1` are published only to TestPyPI
- final release tags such as `1.0.0` are published to both TestPyPI and PyPI

> [!NOTE]
> Publishing requires the repository's configured GitHub Actions environments and trusted publishing settings. Maintainers do not need to upload packages manually with `twine` during the normal release flow.
