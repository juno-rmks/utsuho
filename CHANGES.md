# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.2.0rc2] - 2026-03-21

### Added

- MCP (Model Context Protocol) server support powered by FastMCP.
- The optional `mcp` dependency group and the `utsuho-mcp` console script.
- MCP tools for half-width/full-width and hiragana/katakana conversion.
- MCP usage documentation in the README and Sphinx documentation.

### Changed

- The documentation index now includes the MCP guide.
- Refined the README and documentation wording for the CLI, MCP, and conversion-rule guides.
- The MCP server now starts with a quieter default configuration (`WARNING` log level and no startup banner).

### Fixed

- Added async MCP client tests to cover the exposed MCP tools and their option handling.

## [2.1.2] - 2026-03-18

### Added

- Continuous Integration (CI) workflow using GitHub Actions.
- Release workflow using GitHub Actions to publish packages to TestPyPI and PyPI.

### Changed

- Simplified the `build-system` configuration in `pyproject.toml`.
- Updated the packaging configuration to follow current setuptools practices.
- Reorganized development dependencies into `test`, `docs`, and `dev` extras.
- Adjusted the pylint configuration to allow the intentional design patterns used in the converter classes.
- Excluded `docs/source/conf.py` from Black and isort checks.

### Fixed

- Fixed Windows test failures caused by relying on the platform default encoding in CLI file-based tests.

## [2.1.1] - 2025-10-30

### Changed

- Modernized `pyproject.toml`.
- Replaced autopep8 with Black as the code formatter.
- Standardized string literals to use double quotes.

### Removed

- Support for EOL Python versions (3.8 and 3.9).

## [2.1.0] - 2023-11-12

### Added

- Import support for the hiragana-katakana bidirectional converter.

### Removed

- Support for Python 3.7 (EOL).

## [2.0.0] - 2023-08-25

### Changed

- Renamed `ConverterConfig` to `WidthConverterConfig`.

### Added

- Bidirectional conversion between hiragana and katakana.

## [1.1.2] - 2023-04-23

### Added

- CLI support.

## [1.1.1] - 2023-04-06

### Fixed

- An issue that prevented jQuery from working on Read the Docs.

  See: ["Sphinx 6 is out and has important breaking changes"](https://blog.readthedocs.com/sphinx6-upgrade/).

## [1.1.0] - 2023-04-05

### Added

- Conversion between half-width and full-width spaces.
- Conversion between half-width and full-width symbols.
- Conversion between half-width and full-width digits.
- Conversion between half-width and full-width alphabets.

## [1.0.0] - 2023-04-02

### Added

- Initial public preview release.
