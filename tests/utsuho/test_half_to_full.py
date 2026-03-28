"""
Tests for the HalfToFullConverter class.
"""

import pytest

from utsuho.converters import HalfToFullConverter, WidthConverterConfig

HALF_TO_FULL_BASE_CASES = [
    # Katakana (unvoiced)
    ("ｱ", "ア"),
    ("ｲ", "イ"),
    ("ｳ", "ウ"),
    ("ｴ", "エ"),
    ("ｵ", "オ"),
    ("ｶ", "カ"),
    ("ｷ", "キ"),
    ("ｸ", "ク"),
    ("ｹ", "ケ"),
    ("ｺ", "コ"),
    ("ｻ", "サ"),
    ("ｼ", "シ"),
    ("ｽ", "ス"),
    ("ｾ", "セ"),
    ("ｿ", "ソ"),
    ("ﾀ", "タ"),
    ("ﾁ", "チ"),
    ("ﾂ", "ツ"),
    ("ﾃ", "テ"),
    ("ﾄ", "ト"),
    ("ﾅ", "ナ"),
    ("ﾆ", "ニ"),
    ("ﾇ", "ヌ"),
    ("ﾈ", "ネ"),
    ("ﾉ", "ノ"),
    ("ﾊ", "ハ"),
    ("ﾋ", "ヒ"),
    ("ﾌ", "フ"),
    ("ﾍ", "ヘ"),
    ("ﾎ", "ホ"),
    ("ﾏ", "マ"),
    ("ﾐ", "ミ"),
    ("ﾑ", "ム"),
    ("ﾒ", "メ"),
    ("ﾓ", "モ"),
    ("ﾔ", "ヤ"),
    ("ﾕ", "ユ"),
    ("ﾖ", "ヨ"),
    ("ﾗ", "ラ"),
    ("ﾘ", "リ"),
    ("ﾙ", "ル"),
    ("ﾚ", "レ"),
    ("ﾛ", "ロ"),
    ("ﾜ", "ワ"),
    ("ｦ", "ヲ"),
    ("ﾝ", "ン"),
    # Katakana (unvoiced, small)
    ("ｧ", "ァ"),
    ("ｨ", "ィ"),
    ("ｩ", "ゥ"),
    ("ｪ", "ェ"),
    ("ｫ", "ォ"),
    ("ｯ", "ッ"),
    ("ｬ", "ャ"),
    ("ｭ", "ュ"),
    ("ｮ", "ョ"),
    # Katakana (voiced)
    ("ｶ\uff9e", "ガ"),
    ("ｷ\uff9e", "ギ"),
    ("ｸ\uff9e", "グ"),
    ("ｹ\uff9e", "ゲ"),
    ("ｺ\uff9e", "ゴ"),
    ("ｻ\uff9e", "ザ"),
    ("ｼ\uff9e", "ジ"),
    ("ｽ\uff9e", "ズ"),
    ("ｾ\uff9e", "ゼ"),
    ("ｿ\uff9e", "ゾ"),
    ("ﾀ\uff9e", "ダ"),
    ("ﾁ\uff9e", "ヂ"),
    ("ﾂ\uff9e", "ヅ"),
    ("ﾃ\uff9e", "デ"),
    ("ﾄ\uff9e", "ド"),
    ("ﾊ\uff9e", "バ"),
    ("ﾋ\uff9e", "ビ"),
    ("ﾌ\uff9e", "ブ"),
    ("ﾍ\uff9e", "ベ"),
    ("ﾎ\uff9e", "ボ"),
    ("ﾜ\uff9e", "ヷ"),
    ("ｳ\uff9e", "ヴ"),
    ("ｦ\uff9e", "ヺ"),
    # Katakana (semi-voiced)
    ("ﾊ\uff9f", "パ"),
    ("ﾋ\uff9f", "ピ"),
    ("ﾌ\uff9f", "プ"),
    ("ﾍ\uff9f", "ペ"),
    ("ﾎ\uff9f", "ポ"),
    # Hiragana (voiced and semi-voiced sound marks)
    ("\uff9e", "\u309b"),
    ("\uff9f", "\u309c"),
    # Voiced and semi-voiced sound marks without a predefined full-width composite character
    ("ｱ\uff9e", "ア\u309b"),
    ("ｶ\uff9e\uff9e", "ガ\u309b"),
    ("ｱ\uff9f", "ア\u309c"),
    ("ﾊ\uff9f\uff9f", "パ\u309c"),
    # Variation selectors
    ("\ufe00", "\ufe00"),
    ("\ufe01", "\ufe01"),
    ("\ufe02", "\ufe02"),
    ("\ufe03", "\ufe03"),
    ("\ufe04", "\ufe04"),
    ("\ufe05", "\ufe05"),
    ("\ufe06", "\ufe06"),
    ("\ufe07", "\ufe07"),
    ("\ufe08", "\ufe08"),
    ("\ufe09", "\ufe09"),
    ("\ufe0a", "\ufe0a"),
    ("\ufe0b", "\ufe0b"),
    ("\ufe0c", "\ufe0c"),
    ("\ufe0d", "\ufe0d"),
    ("\ufe0e", "\ufe0e"),
    ("\ufe0f", "\ufe0f"),
    # Invalid variation selector following a convertible character
    ("ｱ\ufe00", "ア\ufe00"),
    # Invalid variation selector not following a convertible character
    ("亜\ufe00", "亜\ufe00"),
]
HALF_TO_FULL_PUNCTUATION_CASES = [
    ("､", "、"),
    ("｡", "。"),
]
HALF_TO_FULL_CORNER_BRACKET_CASES = [
    ("｢", "「"),
    ("｣", "」"),
]
HALF_TO_FULL_CONJUNCTION_MARK_CASES = [
    ("･", "・"),
]
HALF_TO_FULL_LENGTH_MARK_CASES = [
    ("ｰ", "ー"),
]
HALF_TO_FULL_SPACE_CASES = [
    ("\u0020", "\u3000"),
    ("\u00a0", "\u3000"),
]
HALF_TO_FULL_ASCII_SYMBOL_CASES = [
    ("!", "！"),
    ("\"", "＂"),
    ("#", "＃"),
    ("$", "＄"),
    ("%", "％"),
    ("&", "＆"),
    ("'", "＇"),
    ("(", "（"),
    (")", "）"),
    ("*", "＊"),
    ("+", "＋"),
    (",", "，"),
    ("-", "－"),
    (".", "．"),
    ("/", "／"),
    (":", "："),
    (";", "；"),
    ("<", "＜"),
    ("=", "＝"),
    (">", "＞"),
    ("?", "？"),
    ("@", "＠"),
    ("[", "［"),
    ("\\", "＼"),
    ("]", "］"),
    ("^", "＾"),
    ("_", "＿"),
    ("`", "｀"),
    ("{", "｛"),
    ("|", "｜"),
    ("}", "｝"),
    ("~", "\uff5e"),
]
HALF_TO_FULL_ASCII_DIGIT_CASES = [
    ("0", "０"),
    ("1", "１"),
    ("2", "２"),
    ("3", "３"),
    ("4", "４"),
    ("5", "５"),
    ("6", "６"),
    ("7", "７"),
    ("8", "８"),
    ("9", "９"),
    ("0\ufe00", "０\ufe00"),
]
HALF_TO_FULL_ASCII_ALPHABET_CASES = [
    ("A", "Ａ"),
    ("B", "Ｂ"),
    ("C", "Ｃ"),
    ("D", "Ｄ"),
    ("E", "Ｅ"),
    ("F", "Ｆ"),
    ("G", "Ｇ"),
    ("H", "Ｈ"),
    ("I", "Ｉ"),
    ("J", "Ｊ"),
    ("K", "Ｋ"),
    ("L", "Ｌ"),
    ("M", "Ｍ"),
    ("N", "Ｎ"),
    ("O", "Ｏ"),
    ("P", "Ｐ"),
    ("Q", "Ｑ"),
    ("R", "Ｒ"),
    ("S", "Ｓ"),
    ("T", "Ｔ"),
    ("U", "Ｕ"),
    ("V", "Ｖ"),
    ("W", "Ｗ"),
    ("X", "Ｘ"),
    ("Y", "Ｙ"),
    ("Z", "Ｚ"),
    ("a", "ａ"),
    ("b", "ｂ"),
    ("c", "ｃ"),
    ("d", "ｄ"),
    ("e", "ｅ"),
    ("f", "ｆ"),
    ("g", "ｇ"),
    ("h", "ｈ"),
    ("i", "ｉ"),
    ("j", "ｊ"),
    ("k", "ｋ"),
    ("l", "ｌ"),
    ("m", "ｍ"),
    ("n", "ｎ"),
    ("o", "ｏ"),
    ("p", "ｐ"),
    ("q", "ｑ"),
    ("r", "ｒ"),
    ("s", "ｓ"),
    ("t", "ｔ"),
    ("u", "ｕ"),
    ("v", "ｖ"),
    ("w", "ｗ"),
    ("x", "ｘ"),
    ("y", "ｙ"),
    ("z", "ｚ"),
]
HALF_TO_FULL_DEFAULT_CASES = (
    HALF_TO_FULL_BASE_CASES
    + HALF_TO_FULL_PUNCTUATION_CASES
    + HALF_TO_FULL_CORNER_BRACKET_CASES
    + HALF_TO_FULL_CONJUNCTION_MARK_CASES
    + HALF_TO_FULL_LENGTH_MARK_CASES
    + HALF_TO_FULL_SPACE_CASES
    + HALF_TO_FULL_ASCII_SYMBOL_CASES
    + HALF_TO_FULL_ASCII_DIGIT_CASES
    + HALF_TO_FULL_ASCII_ALPHABET_CASES
)


class TestHalfToFullConverter:
    """
    Tests for the HalfToFullConverter class.
    """

    @pytest.mark.parametrize("s,expect", HALF_TO_FULL_DEFAULT_CASES)
    def test_convert(self, s, expect):
        """
        Verify default half-width to full-width conversion behavior.
        """
        cnv = HalfToFullConverter()
        actual = cnv.convert(s)
        assert actual == expect

    @pytest.mark.parametrize("s", [s for s, _ in HALF_TO_FULL_PUNCTUATION_CASES])
    def test_convert_without_punctuation(self, s):
        """
        Verify that punctuation conversion can be disabled.
        """
        cnv = HalfToFullConverter(
            WidthConverterConfig(punctuation=False),
        )
        actual = cnv.convert(s)
        assert actual == s

    @pytest.mark.parametrize("s", [s for s, _ in HALF_TO_FULL_CORNER_BRACKET_CASES])
    def test_convert_without_corner_brucket(self, s):
        """
        Verify that corner bracket conversion can be disabled.
        """
        cnv = HalfToFullConverter(WidthConverterConfig(corner_brucket=False))
        actual = cnv.convert(s)
        assert actual == s

    @pytest.mark.parametrize("s", [s for s, _ in HALF_TO_FULL_CONJUNCTION_MARK_CASES])
    def test_convert_without_conjunction_mark(self, s):
        """
        Verify that conjunction mark conversion can be disabled.
        """
        cnv = HalfToFullConverter(WidthConverterConfig(conjunction_mark=False))
        actual = cnv.convert(s)
        assert actual == s

    @pytest.mark.parametrize("s", [s for s, _ in HALF_TO_FULL_LENGTH_MARK_CASES])
    def test_convert_without_length_mark(self, s):
        """
        Verify that length mark conversion can be disabled.
        """
        cnv = HalfToFullConverter(
            WidthConverterConfig(length_mark=False),
        )
        actual = cnv.convert(s)
        assert actual == s

    @pytest.mark.parametrize("s", [s for s, _ in HALF_TO_FULL_SPACE_CASES])
    def test_convert_without_space(self, s):
        """
        Verify that space conversion can be disabled.
        """
        cnv = HalfToFullConverter(
            WidthConverterConfig(space=False),
        )
        actual = cnv.convert(s)
        assert actual == s

    @pytest.mark.parametrize("s", [s for s, _ in HALF_TO_FULL_ASCII_SYMBOL_CASES])
    def test_convert_without_ascii_symbol(self, s):
        """
        Verify that ASCII symbol conversion can be disabled.
        """
        cnv = HalfToFullConverter(
            WidthConverterConfig(ascii_symbol=False),
        )
        actual = cnv.convert(s)
        assert actual == s

    @pytest.mark.parametrize("s", [s for s, _ in HALF_TO_FULL_ASCII_DIGIT_CASES])
    def test_convert_without_ascii_digit(self, s):
        """
        Verify that ASCII digit conversion can be disabled.
        """
        cnv = HalfToFullConverter(
            WidthConverterConfig(ascii_digit=False),
        )
        actual = cnv.convert(s)
        assert actual == s

    @pytest.mark.parametrize("s", [s for s, _ in HALF_TO_FULL_ASCII_ALPHABET_CASES])
    def test_convert_without_ascii_alphabet(self, s):
        """
        Verify that ASCII alphabet conversion can be disabled.
        """
        cnv = HalfToFullConverter(
            WidthConverterConfig(ascii_alphabet=False),
        )
        actual = cnv.convert(s)
        assert actual == s

    def test_convert_with_invalid_parameter(self):
        """
        Verify that non-string input raises a TypeError.
        """
        cnv = HalfToFullConverter()

        with pytest.raises(TypeError, match="s must be a string."):
            cnv.convert(None)  # type: ignore
