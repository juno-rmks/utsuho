""" Utsuho is an interconverter between Japanese half-width katakana and full-width katakana.
"""
from dataclasses import dataclass

from .maps import (
    full_to_half_conjunction_mark_map,
    full_to_half_corner_bracket_map,
    full_to_half_length_mark_map,
    full_to_half_letter_map,
    full_to_half_punctuation_map,
    full_to_half_voicing_mark_map,
    half_to_full_conjunction_mark_map,
    half_to_full_corner_bracket_map,
    half_to_full_length_mark_map,
    half_to_full_letter_map,
    half_to_full_punctuation_map,
    half_to_full_voicing_mark_map
)

__version__ = '1.0.0'


@dataclass
class ConverterConfig():
    """ Configuration of whether to convert non-katakana characters.

    Parameters
    ----------
    puctuation: bool, default=True
        Whether to convert punctuations.
    corner_brucket: bool, default=True
        Whether to convert corner bruckets.
    conjunction_mark: bool, default=True
        Whether to convert conjunction mark.
    length_mark: bool, default=True
        Whether to convert length mark.
    """
    punctuation: bool = True
    """ Whether to convert punctuations."""
    corner_brucket: bool = True
    """ Whether to convert corner bruckets."""
    conjunction_mark: bool = True
    """ Whether to convert conjunction mark."""
    length_mark: bool = True
    """ Whether to convert length mark."""


class FullToHalfConverter():
    """ Full-width katakana to half-width katakana converter.

    Parameters
    ----------
    config: ConverterConfig, default=ConverterConfig()
        Additional configuration of whether to convert non-katakana letters.
    """

    def __init__(self, config: ConverterConfig = ConverterConfig()) -> None:
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

        while i < len(s):
            cc = s[i]
            in_katakana = cc in full_to_half_letter_map \
                or (in_katakana and cc in full_to_half_voicing_mark_map)

            if cc in full_to_half_voicing_mark_map and not in_katakana:
                converted += cc
                i += 1
                continue

            converted += self._full_to_half_map.get(cc, cc)
            i += 1

        return converted


class HalfToFullConverter():
    """ Half-width katakana to full-width katakana converter.

    Parameters
    ----------
    config: ConverterConfig, default=ConverterConfig()
        Additional configuration of whether to convert non-katakana letters.
    """

    def __init__(self, config: ConverterConfig = ConverterConfig()) -> None:
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

        while i < len(s):
            cc = s[i]
            nc = s[i + 1] if i < len(s) - 1 else None
            v = self._half_to_full_map.get(cc, [cc, None, None])

            if nc == '\uFF9E' and v[1] is not None:
                converted += v[1]
                i += 2
                continue

            if nc == '\uFF9F' and v[2] is not None:
                converted += v[2]
                i += 2
                continue

            converted += v[0]
            i += 1

        return converted
