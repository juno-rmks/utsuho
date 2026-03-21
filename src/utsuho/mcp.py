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
    WidthConverterConfig,
)

mcp = FastMCP("Utsuho")

_hira_to_kata = HiraganaToKatakanaConverter()
_kata_to_hira = KatakanaToHiraganaConverter()


# pylint: disable=R0913,R0917
def _build_width_converter_config(
    punctuation: bool = True,
    corner_brucket: bool = True,
    conjunction_mark: bool = True,
    length_mark: bool = True,
    space: bool = True,
    ascii_symbol: bool = True,
    ascii_digit: bool = True,
    ascii_alphabet: bool = True,
    wave_dash: bool = False,
) -> WidthConverterConfig:
    """
    Build a width conversion configuration for MCP tools.
    """
    return WidthConverterConfig(
        punctuation=punctuation,
        corner_brucket=corner_brucket,
        conjunction_mark=conjunction_mark,
        length_mark=length_mark,
        space=space,
        ascii_symbol=ascii_symbol,
        ascii_digit=ascii_digit,
        ascii_alphabet=ascii_alphabet,
        wave_dash=wave_dash,
    )


@mcp.tool
# pylint: disable=R0913,R0917
def half_to_full(
    text: str,
    punctuation: bool = True,
    corner_brucket: bool = True,
    conjunction_mark: bool = True,
    length_mark: bool = True,
    space: bool = True,
    ascii_symbol: bool = True,
    ascii_digit: bool = True,
    ascii_alphabet: bool = True,
) -> str:
    """
    Convert half-width characters to full-width characters.

    Parameters
    ----------
    text : str
        Text to convert to full-width characters.
    punctuation : bool, default=True
        Whether to convert punctuation marks.
    corner_brucket : bool, default=True
        Whether to convert corner brackets.
    conjunction_mark : bool, default=True
        Whether to convert conjunction marks.
    length_mark : bool, default=True
        Whether to convert length marks.
    space : bool, default=True
        Whether to convert spaces.
    ascii_symbol : bool, default=True
        Whether to convert ASCII symbols.
    ascii_digit : bool, default=True
        Whether to convert ASCII digits.
    ascii_alphabet : bool, default=True
        Whether to convert ASCII alphabets.

    Returns
    -------
    str
        Converted text.
    """
    config = _build_width_converter_config(
        punctuation=punctuation,
        corner_brucket=corner_brucket,
        conjunction_mark=conjunction_mark,
        length_mark=length_mark,
        space=space,
        ascii_symbol=ascii_symbol,
        ascii_digit=ascii_digit,
        ascii_alphabet=ascii_alphabet,
    )
    return HalfToFullConverter(config).convert(text)


@mcp.tool
# pylint: disable=R0913,R0917
def full_to_half(
    text: str,
    punctuation: bool = True,
    corner_brucket: bool = True,
    conjunction_mark: bool = True,
    length_mark: bool = True,
    space: bool = True,
    ascii_symbol: bool = True,
    ascii_digit: bool = True,
    ascii_alphabet: bool = True,
    wave_dash: bool = False,
) -> str:
    """
    Convert full-width characters to half-width characters.

    Parameters
    ----------
    text : str
        Text to convert to half-width characters.
    punctuation : bool, default=True
        Whether to convert punctuation marks.
    corner_brucket : bool, default=True
        Whether to convert corner brackets.
    conjunction_mark : bool, default=True
        Whether to convert conjunction marks.
    length_mark : bool, default=True
        Whether to convert length marks.
    space : bool, default=True
        Whether to convert spaces.
    ascii_symbol : bool, default=True
        Whether to convert ASCII symbols.
    ascii_digit : bool, default=True
        Whether to convert ASCII digits.
    ascii_alphabet : bool, default=True
        Whether to convert ASCII alphabets.
    wave_dash : bool, default=False
        Whether to convert full-width wave dashes to half-width tildes.

    Returns
    -------
    str
        Converted text.
    """
    config = _build_width_converter_config(
        punctuation=punctuation,
        corner_brucket=corner_brucket,
        conjunction_mark=conjunction_mark,
        length_mark=length_mark,
        space=space,
        ascii_symbol=ascii_symbol,
        ascii_digit=ascii_digit,
        ascii_alphabet=ascii_alphabet,
        wave_dash=wave_dash,
    )
    return FullToHalfConverter(config).convert(text)


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
    mcp.run(
        transport="stdio",
        log_level="WARNING",
        show_banner=False,
    )
