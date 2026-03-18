# Roadmap

This roadmap outlines the planned direction of the Utsuho project.

Utsuho aims to remain a **lightweight, deterministic, pure-Python
library for Japanese text normalization**.

The project focuses on:

- deterministic character-level transformations
- minimal dependencies
- predictable behavior suitable for preprocessing and search
  normalization

Utsuho intentionally avoids dictionary-based processing and heavy
linguistic frameworks.

## Near Term

### MCP Interface

Provide a Model Context Protocol (MCP) interface so that Utsuho can be
used as a tool from AI systems.

Planned features:

- MCP server implementation
- four conversion tools
  - `half_to_full`
  - `full_to_half`
  - `hiragana_to_katakana`
  - `katakana_to_hiragana`
- optional dependency (`utsuho[mcp]`)
- stdio transport support

This enables AI systems and agents to normalize Japanese text using
Utsuho.

### Kana → Romaji Conversion

Add deterministic kana-to-romaji conversion.

Goals:

- deterministic mapping
- no dictionary or morphological analysis
- suitable for indexing and search preprocessing

Expected features:

- Hepburn style output
- handling of:
  - small kana
  - long vowels
  - sokuon (っ)
  - yōon (きゃ, しゃ, etc.)

## Mid Term

### Iteration Mark Expansion

Add support for expanding Japanese iteration marks.

Examples:

    時々 → 時時
    いろゝ → いろろ
    サヽキ → ササキ

Supported characters:

    ゝ ゞ ヽ ヾ

This feature remains deterministic and does not require dictionaries.

### Performance Improvements

Continue improving performance while keeping the implementation pure
Python.

Possible improvements include:

- optimized string building
- reduced allocations
- faster lookup paths

Benchmarks will be maintained to detect performance regressions.

## Long Term

### API Stabilization

Review and refine the public API as the project grows.

Possible improvements include:

- improved configuration design
- clearer separation between normalization types
- better extensibility for future converters

Breaking API changes, if necessary, would be introduced in a future
major release.

## Non-Goals

To keep the project focused and maintainable, Utsuho intentionally
avoids:

- dictionary-based processing
- morphological analysis
- heavy linguistic frameworks
- native extensions

The project will remain a **pure-Python deterministic normalization
library**.
