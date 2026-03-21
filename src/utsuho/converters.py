"""
Converters.
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
    kana_to_hira_map,
)


@dataclass
class WidthConverterConfig:
    """
    Configuration of whether to convert non-katakana characters.

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


class FullToHalfConverter:
    """
    Full-width katakana to half-width katakana converter.

    Parameters
    ----------
    config: WidthConverterConfig, default=WidthConverterConfig()
        Additional configuration of whether to convert non-katakana letters.
    """

    _variation_selectors = frozenset(chr(c) for c in range(0xFE00, 0xFE0F + 1))
    _punctuation_variants = frozenset(
        [
            "\uff01",
            "\uff0c",
            "\uff0e",
            "\uff1a",
            "\uff1b",
            "\uff1f",
        ]
    )
    _base_map = {
        **full_to_half_letter_map,
        **full_to_half_voicing_mark_map,
    }
    _optional_maps = (
        ("punctuation", full_to_half_punctuation_map),
        ("corner_brucket", full_to_half_corner_bracket_map),
        ("conjunction_mark", full_to_half_conjunction_mark_map),
        ("length_mark", full_to_half_length_mark_map),
        ("space", full_to_half_space_map),
        ("ascii_symbol", full_to_half_ascii_symbol_map),
        ("ascii_digit", full_to_half_ascii_digit_map),
        ("ascii_alphabet", full_to_half_ascii_alphabet_map),
        ("wave_dash", full_to_half_wave_dash),
    )

    def __init__(
        self,
        config: WidthConverterConfig = WidthConverterConfig(),
    ) -> None:
        self._full_to_half_map = self._build_map(config)

    @classmethod
    def _build_map(
        cls,
        config: WidthConverterConfig,
    ) -> dict[str, str]:
        converter_map = dict(cls._base_map)

        for attr_name, mapping in cls._optional_maps:
            if getattr(config, attr_name):
                converter_map.update(mapping)

        return converter_map

    def convert(
        self,
        s: str,
    ) -> str:
        """
        Convert full-width katakana to half-width katakana.

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
            raise TypeError("s must be a string.")

        converted = []
        i = 0
        in_katakana = False

        while i < len(s):
            cc = s[i]
            nc = s[i + 1] if i < len(s) - 1 else None
            v = self._full_to_half_map.get(cc, None)

            if v is None:
                in_katakana = False
                converted.append(cc)
                i += 1
                continue

            in_katakana = cc in full_to_half_letter_map or (
                in_katakana and cc in full_to_half_voicing_mark_map
            )

            if not in_katakana and cc in full_to_half_voicing_mark_map:
                converted.append(cc)
                i += 1
                continue

            converted.append(v)
            i += 1

            if nc == "\ufe00" and cc == "\uff10":
                converted.append("\ufe00")
                i += 1
            elif nc in {"\ufe00", "\ufe01"} and cc in self._punctuation_variants:
                i += 1
            elif nc in self._variation_selectors:
                i += 1

        return "".join(converted)


class HalfToFullConverter:
    """
    Half-width katakana to full-width katakana converter.

    Parameters
    ----------
    config: WidthConverterConfig, default=WidthConverterConfig()
        Additional configuration of whether to convert non-katakana letters.
    """

    _variation_selectors = frozenset(chr(c) for c in range(0xFE00, 0xFE0F + 1))
    _base_map = {
        **half_to_full_letter_map,
        **half_to_full_voicing_mark_map,
    }
    _optional_maps = (
        ("punctuation", half_to_full_punctuation_map),
        ("corner_brucket", half_to_full_corner_bracket_map),
        ("conjunction_mark", half_to_full_conjunction_mark_map),
        ("length_mark", half_to_full_length_mark_map),
        ("space", half_to_full_space_map),
        ("ascii_symbol", half_to_full_ascii_symbol_map),
        ("ascii_digit", half_to_full_ascii_digit_map),
        ("ascii_alphabet", half_to_full_ascii_alphabet_map),
    )

    def __init__(
        self,
        config: WidthConverterConfig = WidthConverterConfig(),
    ) -> None:
        self._half_to_full_map = self._build_map(config)

    @classmethod
    def _build_map(
        cls,
        config: WidthConverterConfig,
    ) -> dict[str, str | tuple[str, str | None, str | None]]:
        converter_map = dict(cls._base_map)

        for attr_name, mapping in cls._optional_maps:
            if getattr(config, attr_name):
                converter_map.update(mapping)

        return converter_map

    def convert(
        self,
        s: str,
    ) -> str:
        """
        Convert half-width katakana to full-width katakana.

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
            raise TypeError("s must be a string.")

        converted = []
        i = 0

        while i < len(s):
            cc = s[i]
            nc = s[i + 1] if i < len(s) - 1 else None
            v = self._half_to_full_map.get(cc, None)

            if v is None:
                converted.append(cc)
                i += 1
                continue

            if cc in half_to_full_letter_map:
                if nc == "\uff9e" and v[1] is not None:
                    converted.append(v[1])
                    i += 2
                elif nc == "\uff9f" and v[2] is not None:
                    converted.append(v[2])
                    i += 2
                else:
                    converted.append(v[0])
                    i += 1

                continue

            converted.append(v)
            i += 1

            if nc == "\ufe00" and cc == "\u0030":
                converted.append("\ufe00")
                i += 1
            elif nc in self._variation_selectors:
                i += 1

        return "".join(converted)


class HiraganaToKatakanaConverter:
    """
    Hiragana to katakana converter.
    """

    def convert(
        self,
        s: str,
    ) -> str:
        """
        Convert hiragana to katakana.

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
            raise TypeError("s must be a string.")

        return "".join([hira_to_kana_map.get(cc, cc) for cc in s])


class KatakanaToHiraganaConverter:
    """
    Katakana to hiragana converter.
    """

    def convert(
        self,
        s: str,
    ) -> str:
        """
        Convert katakana to hiragana.

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
            raise TypeError("s must be a string.")

        return "".join([kana_to_hira_map.get(cc, cc) for cc in s])
