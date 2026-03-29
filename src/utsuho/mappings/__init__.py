"""
Mapping definitions for deterministic Japanese text conversion.
"""

from .common import KanaLetterMapping, SimpleCharacterMap
from .kana import hira_to_kana_map, kana_to_hira_map
from .width import (
    full_to_half_ascii_alphabet_map,
    full_to_half_ascii_digit_map,
    full_to_half_ascii_symbol_map,
    full_to_half_conjunction_mark_map,
    full_to_half_corner_bracket_map,
    full_to_half_length_mark_map,
    full_to_half_letter_map,
    full_to_half_punctuation_map,
    full_to_half_space_map,
    full_to_half_voicing_mark_map,
    full_to_half_wave_dash,
    half_to_full_ascii_alphabet_map,
    half_to_full_ascii_digit_map,
    half_to_full_ascii_symbol_map,
    half_to_full_conjunction_mark_map,
    half_to_full_corner_bracket_map,
    half_to_full_length_mark_map,
    half_to_full_letter_map,
    half_to_full_punctuation_map,
    half_to_full_space_map,
    half_to_full_voicing_mark_map,
)

__all__ = [
    "KanaLetterMapping",
    "SimpleCharacterMap",
    "full_to_half_ascii_alphabet_map",
    "full_to_half_ascii_digit_map",
    "full_to_half_ascii_symbol_map",
    "full_to_half_conjunction_mark_map",
    "full_to_half_corner_bracket_map",
    "full_to_half_length_mark_map",
    "full_to_half_letter_map",
    "full_to_half_punctuation_map",
    "full_to_half_space_map",
    "full_to_half_voicing_mark_map",
    "full_to_half_wave_dash",
    "half_to_full_ascii_alphabet_map",
    "half_to_full_ascii_digit_map",
    "half_to_full_ascii_symbol_map",
    "half_to_full_conjunction_mark_map",
    "half_to_full_corner_bracket_map",
    "half_to_full_length_mark_map",
    "half_to_full_letter_map",
    "half_to_full_punctuation_map",
    "half_to_full_space_map",
    "half_to_full_voicing_mark_map",
    "hira_to_kana_map",
    "kana_to_hira_map",
]
