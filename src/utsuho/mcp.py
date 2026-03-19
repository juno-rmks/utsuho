"""
Model Context Protocol (MCP) server for Utsuho.

This module exposes Utsuho's text conversion utilities as MCP tools.
"""

from fastmcp import FastMCP

from .converters import (
    FullToHalfConverter,
    HalfToFullConverter,
    HiraganaToKatakanaConverter,
    KatakanaToHiraganaConverter,
)

mcp = FastMCP("Utsuho")

_half_to_full = HalfToFullConverter()
_full_to_half = FullToHalfConverter()
_hira_to_kata = HiraganaToKatakanaConverter()
_kata_to_hira = KatakanaToHiraganaConverter()


@mcp.tool
def half_to_full(text: str) -> str:
    """
    Convert half-width characters to full-width characters.

    Parameters
    ----------
    text : str
        Text to convert to full-width characters.

    Returns
    -------
    str
        Converted text.
    """
    return _half_to_full.convert(text)


@mcp.tool
def full_to_half(text: str) -> str:
    """
    Convert full-width characters to half-width characters.

    Parameters
    ----------
    text : str
        Text to convert to half-width characters.

    Returns
    -------
    str
        Converted text.
    """
    return _full_to_half.convert(text)


@mcp.tool
def hiragana_to_katakana(text: str) -> str:
    """
    Convert hiragana to katakana.

    Parameters
    ----------
    text : str
        Text to convert to katakana.

    Returns
    -------
    str
        Converted text.
    """
    return _hira_to_kata.convert(text)


@mcp.tool
def katakana_to_hiragana(text: str) -> str:
    """
    Convert katakana to hiragana.

    Parameters
    ----------
    text : str
        Text to convert to hiragana.

    Returns
    -------
    str
        Converted text.
    """
    return _kata_to_hira.convert(text)


def main() -> None:
    """
    Run the Utsuho MCP server.
    """
    mcp.run()
