""" Converters.
"""
from dataclasses import dataclass

from .maps import (
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
    hira_to_kana_map,
    kana_to_hira_map
)


@dataclass
class WidthConverterConfig():
    """ Configuration of whether to convert non-katakana characters.

    Parameters
    ----------
    punctuation: bool, default=True
        Whether to convert punctuations.
    corner_brucket: bool, default=True
        Whether to convert corner bruckets.
    conjunction_mark: bool, default=True
        Whether to convert conjunction mark.
    length_mark: bool, default=True
        Whether to convert length mark.
    space: bool, default=True
        Whether to convert spaces.
    ascii_symbol: bool, default=True
        Whether to convert ASCII symbols.
    ascii_alphabet: bool, default=True
        Whether to convert ASCII alphabets.
    ascii_digit: bool, default=True
        Whether to convert ASCII digits.
    wave_dash: bool, default=True
        Whether to convert full-width wave dash to half-width tilde.
    """
    punctuation: bool = True
    """ Whether to convert punctuations."""
    corner_brucket: bool = True
    """ Whether to convert corner bruckets."""
    conjunction_mark: bool = True
    """ Whether to convert conjunction mark."""
    length_mark: bool = True
    """ Whether to convert length mark."""
    space: bool = True
    """ Whether to convert spaces. """
    ascii_symbol: bool = True
    """ Whether to convert ASCII symbols. """
    ascii_alphabet: bool = True
    """ Whether to convert ASCII alphabets. """
    ascii_digit: bool = True
    """ Whether to convert ASCII digits."""
    wave_dash: bool = False
    """ Whether to convert full-width wave dash to half-width tilde. """


class FullToHalfConverter():
    """ Full-width katakana to half-width katakana converter.

    Parameters
    ----------
    config: WidthConverterConfig, default=WidthConverterConfig()
        Additional configuration of whether to convert non-katakana letters.
    """

    def __init__(self, config: WidthConverterConfig = WidthConverterConfig()) -> None:
        self._full_to_half_map = {
            **full_to_half_letter_map,
            **full_to_half_voicing_mark_map,
        }

        if config.punctuation:
            self._full_to_half_map.update(**full_to_half_punctuation_map)

        if config.corner_brucket:
            self._full_to_half_map.update(**full_to_half_corner_bracket_map)

        if config.conjunction_mark:
            self._full_to_half_map.update(**full_to_half_conjunction_mark_map)

        if config.length_mark:
            self._full_to_half_map.update(**full_to_half_length_mark_map)

        if config.space:
            self._full_to_half_map.update(**full_to_half_space_map)

        if config.ascii_symbol:
            self._full_to_half_map.update(**full_to_half_ascii_symbol_map)

        if config.ascii_digit:
            self._full_to_half_map.update(**full_to_half_ascii_digit_map)

        if config.ascii_alphabet:
            self._full_to_half_map.update(**full_to_half_ascii_alphabet_map)

        if config.wave_dash:
            self._full_to_half_map.update(**full_to_half_wave_dash)

    def convert(self, s: str) -> str:
        """ Convert full-width katakana to half-width katakana.

        Parameters
        ----------
        s: str
            String containing characters to convert to half-width katakana.

        Returns
        -------
        str
            String after conversion.
        """
        if not isinstance(s, str):
            raise TypeError('s must be a string.')

        converted = ''
        i = 0
        in_katakana = False
        variation_selectors = [chr(c) for c in range(0xFE00, 0xFE0F + 1)]

        while i < len(s):
            cc = s[i]
            nc = s[i + 1] if i < len(s) - 1 else None
            v = self._full_to_half_map.get(cc, None)

            if v is None:
                in_katakana = False
                converted += cc
                i += 1
                continue

            in_katakana = cc in full_to_half_letter_map \
                or (in_katakana and cc in full_to_half_voicing_mark_map)

            if not in_katakana and cc in full_to_half_voicing_mark_map:
                converted += cc
                i += 1
                continue

            converted += v
            i += 1

            if nc == '\uFE00' and cc == '\uFF10':
                converted += '\uFE00'
                i += 1
            elif nc in ['\uFE00', '\uFE01'] and cc in ['\uFF01', '\uFF0C', '\uFF0E', '\uFF1A', '\uFF1B', '\uFF1F']:
                i += 1
            elif nc in variation_selectors:
                i += 1

        return converted


class HalfToFullConverter():
    """ Half-width katakana to full-width katakana converter.

    Parameters
    ----------
    config: WidthConverterConfig, default=WidthConverterConfig()
        Additional configuration of whether to convert non-katakana letters.
    """

    def __init__(self, config: WidthConverterConfig = WidthConverterConfig()) -> None:
        self._half_to_full_map = {
            **half_to_full_letter_map,
            **half_to_full_voicing_mark_map,
        }

        if config.punctuation:
            self._half_to_full_map.update(**half_to_full_punctuation_map)

        if config.corner_brucket:
            self._half_to_full_map.update(**half_to_full_corner_bracket_map)

        if config.conjunction_mark:
            self._half_to_full_map.update(**half_to_full_conjunction_mark_map)

        if config.length_mark:
            self._half_to_full_map.update(**half_to_full_length_mark_map)

        if config.space:
            self._half_to_full_map.update(**half_to_full_space_map)

        if config.ascii_symbol:
            self._half_to_full_map.update(**half_to_full_ascii_symbol_map)

        if config.ascii_digit:
            self._half_to_full_map.update(**half_to_full_ascii_digit_map)

        if config.ascii_alphabet:
            self._half_to_full_map.update(**half_to_full_ascii_alphabet_map)

    def convert(self, s: str) -> str:
        """ Convert half-width katakana to full-width katakana.

        Parameters
        ----------
        s: str
            String containing characters to convert to full-width katakana.

        Returns
        -------
        str
            String after conversion.
        """
        if not isinstance(s, str):
            raise TypeError('s must be a string.')

        converted = ''
        i = 0
        variation_selectors = [chr(c) for c in range(0xFE00, 0xFE0F + 1)]

        while i < len(s):
            cc = s[i]
            nc = s[i + 1] if i < len(s) - 1 else None
            v = self._half_to_full_map.get(cc, None)

            if v is None:
                converted += cc
                i += 1
                continue

            if cc in half_to_full_letter_map:
                if nc == '\uFF9E' and v[1] is not None:
                    converted += v[1]
                    i += 2
                elif nc == '\uFF9F' and v[2] is not None:
                    converted += v[2]
                    i += 2
                else:
                    converted += v[0]
                    i += 1

                continue

            converted += v
            i += 1

            if nc == '\uFE00' and cc == '\u0030':
                converted += '\uFE00'
                i += 1
            elif nc in variation_selectors:
                i += 1

        return converted


class HiraganaToKatakanaConverter():
    """ Hiragana to katakana converter.
    """

    def __init__(self) -> None:
        self._hira_to_kata_map = {}

    def convert(self, s: str) -> str:
        """ Convert hiragana to katakana.

        Parameters
        ----------
        s: str
            String containing characters to convert katakana.

        Returns
        -------
        str
            String after conversion.
        """
        if not isinstance(s, str):
            raise TypeError('s must be a string.')

        return ''.join([hira_to_kana_map.get(cc, cc) for cc in s])


class KatakanaToHiraganaConverter():
    """ Katakana to hiragana converter.
    """

    def __init__(self) -> None:
        self._kata_to_hira_map = {}

    def convert(self, s: str) -> str:
        """ Convert katakana to hiragana.

        Parameters
        ----------
        s: str
            String containing characters to convert hiragana.

        Returns
        -------
        str
            String after conversion.
        """
        if not isinstance(s, str):
            raise TypeError('s must be a string.')

        return ''.join([kana_to_hira_map.get(cc, cc) for cc in s])
