# MCP (Model Context Protocol)

Utsuho provides a Model Context Protocol (MCP) server that exposes its text conversion utilities as tools.

This allows Utsuho to be integrated with MCP-compatible clients such as AI agents, editors, and developer tools.

## Overview

The MCP server wraps Utsuho's deterministic text conversion functions and makes them available as independent tools.

All conversions are:

- deterministic
- character-level
- context-independent

This makes Utsuho suitable for preprocessing and normalization tasks in AI workflows.

## Installation

Install Utsuho with the `mcp` extra:

```sh
pip install "Utsuho[mcp]"
```

## Running the Server

Start the MCP server using:

```sh
utsuho-mcp
```

The server runs over stdio.

## Available Tools

The following tools are provided.

### half_to_full

Convert half-width text to full-width text.

**Input**

```text
text: str
```

**Output**

```text
str
```

### full_to_half

Convert full-width text to half-width text.

**Input**

```text
text: str
```

**Output**

```text
str
```

### hiragana_to_katakana

Convert hiragana to katakana.

**Input**

```text
text: str
```

**Output**

```text
str
```

### katakana_to_hiragana

Convert katakana to hiragana.

**Input**

```text
text: str
```

**Output**

```text
str
```

## Design Notes

- Each tool corresponds directly to a converter class in Utsuho.
- Tools are intentionally minimal and accept only a single `text` parameter.
- No context or state is maintained between calls.
- Configuration options are not exposed in the initial version to keep the interface simple.

## Use Cases

Typical use cases include:

- Normalizing Japanese text before indexing or search
- Preprocessing user input in AI applications
- Converting text within automated tool-based workflows
- Ensuring consistent representation of kana and width variants

## Future Enhancements

Planned improvements may include:

- Optional configuration parameters for width conversion
- Additional normalization features (e.g., romanization)
- Extended MCP capabilities such as resources or prompts
