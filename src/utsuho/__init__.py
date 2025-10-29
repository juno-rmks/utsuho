"""
Utsuho is an interconverter between Japanese half-width katakana and full-width
katakana.
"""

from .converters import (
    FullToHalfConverter,
    HalfToFullConverter,
    HiraganaToKatakanaConverter,
    KatakanaToHiraganaConverter,
    WidthConverterConfig,
)

__version__ = "2.1.1"
