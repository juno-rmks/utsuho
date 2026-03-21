"""
Converters for deterministic Japanese text normalization.
"""

from dataclasses import dataclass

from .maps import (
    KanaLetterMapping,
    SimpleCharacterMap,
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

HalfToFullMap = dict[str, str | KanaLetterMapping]


@dataclass(slots=True)
class WidthConverterConfig:
    """
    Configuration for converting non-katakana characters.

    Parameters
    ----------
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
    ascii_alphabet : bool, default=True
        Whether to convert ASCII alphabets.
    ascii_digit : bool, default=True
        Whether to convert ASCII digits.
    wave_dash : bool, default=False
        Whether to convert full-width wave dash to half-width tilde.
    """

    punctuation: bool = True
    """Whether to convert punctuation marks."""
    corner_brucket: bool = True
    """Whether to convert corner brackets."""
    conjunction_mark: bool = True
    """Whether to convert conjunction marks."""
    length_mark: bool = True
    """Whether to convert length marks."""
    space: bool = True
    """Whether to convert spaces."""
    ascii_symbol: bool = True
    """Whether to convert ASCII symbols."""
    ascii_alphabet: bool = True
    """Whether to convert ASCII alphabets."""
    ascii_digit: bool = True
    """Whether to convert ASCII digits."""
    wave_dash: bool = False
    """Whether to convert full-width wave dashes to half-width tildes."""


class FullToHalfConverter:
    """
    Full-width katakana to half-width katakana converter.

    Parameters
    ----------
    config : WidthConverterConfig, optional
        Additional configuration of whether to convert non-katakana letters.
    """

    _VARIATION_SELECTORS = frozenset(chr(c) for c in range(0xFE00, 0xFE0F + 1))
    _VARIATION_SELECTOR_0 = "\ufe00"
    _VARIATION_SELECTOR_1 = "\ufe01"
    _FULLWIDTH_ZERO = "\uff10"
    _PUNCTUATION_VARIANTS = frozenset(
        [
            "\uff01",
            "\uff0c",
            "\uff0e",
            "\uff1a",
            "\uff1b",
            "\uff1f",
        ]
    )
    _BASE_MAP = {
        **full_to_half_letter_map,
        **full_to_half_voicing_mark_map,
    }
    _OPTIONAL_MAPS = (
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
        config: WidthConverterConfig | None = None,
    ) -> None:
        if config is None:
            config = WidthConverterConfig()

        self._full_to_half_map = self._build_map(config)

    @classmethod
    def _build_map(
        cls,
        config: WidthConverterConfig,
    ) -> SimpleCharacterMap:
        converter_map = dict(cls._BASE_MAP)

        for attr_name, mapping in cls._OPTIONAL_MAPS:
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
        s : str
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
        n = len(s)
        in_katakana = False

        while i < n:
            cc = s[i]
            nc = s[i + 1] if i < n - 1 else None
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

            if nc == self._VARIATION_SELECTOR_0 and cc == self._FULLWIDTH_ZERO:
                converted.append(self._VARIATION_SELECTOR_0)
                i += 1
            elif nc in {
                self._VARIATION_SELECTOR_0,
                self._VARIATION_SELECTOR_1,
            } and cc in self._PUNCTUATION_VARIANTS:
                i += 1
            elif nc in self._VARIATION_SELECTORS:
                i += 1

        return "".join(converted)


class HalfToFullConverter:
    """
    Half-width katakana to full-width katakana converter.

    Parameters
    ----------
    config : WidthConverterConfig, optional
        Additional configuration of whether to convert non-katakana letters.
    """

    _VARIATION_SELECTORS = frozenset(chr(c) for c in range(0xFE00, 0xFE0F + 1))
    _VARIATION_SELECTOR_0 = "\ufe00"
    _HALFWIDTH_ZERO = "\u0030"
    _VOICED_MARK = "\uff9e"
    _SEMI_VOICED_MARK = "\uff9f"
    _BASE_MAP = {
        **half_to_full_letter_map,
        **half_to_full_voicing_mark_map,
    }
    _OPTIONAL_MAPS = (
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
        config: WidthConverterConfig | None = None,
    ) -> None:
        if config is None:
            config = WidthConverterConfig()

        self._half_to_full_map = self._build_map(config)

    @classmethod
    def _build_map(
        cls,
        config: WidthConverterConfig,
    ) -> HalfToFullMap:
        converter_map = dict(cls._BASE_MAP)

        for attr_name, mapping in cls._OPTIONAL_MAPS:
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
        s : str
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
        n = len(s)

        while i < n:
            cc = s[i]
            nc = s[i + 1] if i < n - 1 else None
            v = self._half_to_full_map.get(cc, None)

            if v is None:
                converted.append(cc)
                i += 1
                continue

            if cc in half_to_full_letter_map:
                base, voiced, semi_voiced = v

                if nc == self._VOICED_MARK and voiced is not None:
                    converted.append(voiced)
                    i += 2
                elif nc == self._SEMI_VOICED_MARK and semi_voiced is not None:
                    converted.append(semi_voiced)
                    i += 2
                else:
                    converted.append(base)
                    i += 1

                continue

            converted.append(v)
            i += 1

            if nc == self._VARIATION_SELECTOR_0 and cc == self._HALFWIDTH_ZERO:
                converted.append(self._VARIATION_SELECTOR_0)
                i += 1
            elif nc in self._VARIATION_SELECTORS:
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
        s : str
            String containing characters to convert to katakana.

        Returns
        -------
        str
            String after conversion.
        """
        if not isinstance(s, str):
            raise TypeError("s must be a string.")

        return "".join(hira_to_kana_map.get(cc, cc) for cc in s)


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
        s : str
            String containing characters to convert to hiragana.

        Returns
        -------
        str
            String after conversion.
        """
        if not isinstance(s, str):
            raise TypeError("s must be a string.")

        return "".join(kana_to_hira_map.get(cc, cc) for cc in s)
