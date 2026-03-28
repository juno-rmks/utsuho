"""
Tests for the FullToHalfConverter class.
"""

import pytest

from utsuho.converters import FullToHalfConverter, WidthConverterConfig

FULL_TO_HALF_BASE_CASES = [
    # Katakana (unvoiced)
    ("ア", "ｱ"),
    ("イ", "ｲ"),
    ("ウ", "ｳ"),
    ("エ", "ｴ"),
    ("オ", "ｵ"),
    ("カ", "ｶ"),
    ("キ", "ｷ"),
    ("ク", "ｸ"),
    ("ケ", "ｹ"),
    ("コ", "ｺ"),
    ("サ", "ｻ"),
    ("シ", "ｼ"),
    ("ス", "ｽ"),
    ("セ", "ｾ"),
    ("ソ", "ｿ"),
    ("タ", "ﾀ"),
    ("チ", "ﾁ"),
    ("ツ", "ﾂ"),
    ("テ", "ﾃ"),
    ("ト", "ﾄ"),
    ("ナ", "ﾅ"),
    ("ニ", "ﾆ"),
    ("ヌ", "ﾇ"),
    ("ネ", "ﾈ"),
    ("ノ", "ﾉ"),
    ("ハ", "ﾊ"),
    ("ヒ", "ﾋ"),
    ("フ", "ﾌ"),
    ("ヘ", "ﾍ"),
    ("ホ", "ﾎ"),
    ("マ", "ﾏ"),
    ("ミ", "ﾐ"),
    ("ム", "ﾑ"),
    ("メ", "ﾒ"),
    ("モ", "ﾓ"),
    ("ヤ", "ﾔ"),
    ("ユ", "ﾕ"),
    ("ヨ", "ﾖ"),
    ("ラ", "ﾗ"),
    ("リ", "ﾘ"),
    ("ル", "ﾙ"),
    ("レ", "ﾚ"),
    ("ロ", "ﾛ"),
    ("ワ", "ﾜ"),
    ("ヰ", "ヰ"),
    ("ヱ", "ヱ"),
    ("ヲ", "ｦ"),
    ("ン", "ﾝ"),
    # Katakana (unvoiced, small)
    ("ァ", "ｧ"),
    ("ィ", "ｨ"),
    ("ゥ", "ｩ"),
    ("ェ", "ｪ"),
    ("ォ", "ｫ"),
    ("ッ", "ｯ"),
    ("ャ", "ｬ"),
    ("ュ", "ｭ"),
    ("ョ", "ｮ"),
    ("ヮ", "ヮ"),
    ("ヵ", "ヵ"),
    ("ヶ", "ヶ"),
    # Katakana (voiced)
    ("ガ", "ｶ\uff9e"),
    ("ギ", "ｷ\uff9e"),
    ("グ", "ｸ\uff9e"),
    ("ゲ", "ｹ\uff9e"),
    ("ゴ", "ｺ\uff9e"),
    ("ザ", "ｻ\uff9e"),
    ("ジ", "ｼ\uff9e"),
    ("ズ", "ｽ\uff9e"),
    ("ゼ", "ｾ\uff9e"),
    ("ゾ", "ｿ\uff9e"),
    ("ダ", "ﾀ\uff9e"),
    ("ヂ", "ﾁ\uff9e"),
    ("ヅ", "ﾂ\uff9e"),
    ("デ", "ﾃ\uff9e"),
    ("ド", "ﾄ\uff9e"),
    ("バ", "ﾊ\uff9e"),
    ("ビ", "ﾋ\uff9e"),
    ("ブ", "ﾌ\uff9e"),
    ("ベ", "ﾍ\uff9e"),
    ("ボ", "ﾎ\uff9e"),
    ("ヷ", "ﾜ\uff9e"),
    ("ヸ", "ヸ"),
    ("ヴ", "ｳ\uff9e"),
    ("ヹ", "ヹ"),
    ("ヺ", "ｦ\uff9e"),
    # Katakana (semi-voiced)
    ("パ", "ﾊ\uff9f"),
    ("ピ", "ﾋ\uff9f"),
    ("プ", "ﾌ\uff9f"),
    ("ペ", "ﾍ\uff9f"),
    ("ポ", "ﾎ\uff9f"),
    # Katakana (unvoiced) + hiragana voiced sound mark
    ("カ\u309b", "ｶ\uff9e"),
    ("キ\u309b", "ｷ\uff9e"),
    ("ク\u309b", "ｸ\uff9e"),
    ("ケ\u309b", "ｹ\uff9e"),
    ("コ\u309b", "ｺ\uff9e"),
    ("サ\u309b", "ｻ\uff9e"),
    ("シ\u309b", "ｼ\uff9e"),
    ("ス\u309b", "ｽ\uff9e"),
    ("セ\u309b", "ｾ\uff9e"),
    ("ソ\u309b", "ｿ\uff9e"),
    ("タ\u309b", "ﾀ\uff9e"),
    ("チ\u309b", "ﾁ\uff9e"),
    ("ツ\u309b", "ﾂ\uff9e"),
    ("テ\u309b", "ﾃ\uff9e"),
    ("ト\u309b", "ﾄ\uff9e"),
    ("ハ\u309b", "ﾊ\uff9e"),
    ("ヒ\u309b", "ﾋ\uff9e"),
    ("フ\u309b", "ﾌ\uff9e"),
    ("ヘ\u309b", "ﾍ\uff9e"),
    ("ホ\u309b", "ﾎ\uff9e"),
    ("ウ\u309b", "ｳ\uff9e"),
    ("ワ\u309b", "ﾜ\uff9e"),
    ("ヰ\u309b", "ヰ\u309b"),
    ("ヱ\u309b", "ヱ\u309b"),
    ("ヲ\u309b", "ｦ\uff9e"),
    # Katakana (unvoiced) + hiragana semi-voiced sound mark
    ("ハ\u309c", "ﾊ\uff9f"),
    ("ヒ\u309c", "ﾋ\uff9f"),
    ("フ\u309c", "ﾌ\uff9f"),
    ("ヘ\u309c", "ﾍ\uff9f"),
    ("ホ\u309c", "ﾎ\uff9f"),
    # Katakana (unvoiced) + hiragana voiced sound mark (combining mark)
    ("カ\u3099", "ｶ\uff9e"),
    ("キ\u3099", "ｷ\uff9e"),
    ("ク\u3099", "ｸ\uff9e"),
    ("ケ\u3099", "ｹ\uff9e"),
    ("コ\u3099", "ｺ\uff9e"),
    ("サ\u3099", "ｻ\uff9e"),
    ("シ\u3099", "ｼ\uff9e"),
    ("ス\u3099", "ｽ\uff9e"),
    ("セ\u3099", "ｾ\uff9e"),
    ("ソ\u3099", "ｿ\uff9e"),
    ("タ\u3099", "ﾀ\uff9e"),
    ("チ\u3099", "ﾁ\uff9e"),
    ("ツ\u3099", "ﾂ\uff9e"),
    ("テ\u3099", "ﾃ\uff9e"),
    ("ト\u3099", "ﾄ\uff9e"),
    ("ハ\u3099", "ﾊ\uff9e"),
    ("ヒ\u3099", "ﾋ\uff9e"),
    ("フ\u3099", "ﾌ\uff9e"),
    ("ヘ\u3099", "ﾍ\uff9e"),
    ("ホ\u3099", "ﾎ\uff9e"),
    ("ウ\u3099", "ｳ\uff9e"),
    ("ワ\u3099", "ﾜ\uff9e"),
    ("ヰ\u3099", "ヰ\u3099"),
    ("ヱ\u3099", "ヱ\u3099"),
    ("ヲ\u3099", "ｦ\uff9e"),
    # Katakana (unvoiced) + hiragana semi-voiced sound mark (combining mark)
    ("ハ\u309a", "ﾊ\uff9f"),
    ("ヒ\u309a", "ﾋ\uff9f"),
    ("フ\u309a", "ﾌ\uff9f"),
    ("ヘ\u309a", "ﾍ\uff9f"),
    ("ホ\u309a", "ﾎ\uff9f"),
    # Katakana (other)
    ("゠", "゠"),
    ("ヽ", "ヽ"),
    ("ヾ", "ヾ"),
    ("ヿ", "ヿ"),
    # Hiragana (voiced and semi-voiced sound marks)
    ("\u309b", "\u309b"),
    ("\u309c", "\u309c"),
    ("\u3099", "\u3099"),
    ("\u309a", "\u309a"),
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
    # Voiced and semi-voiced sound marks following katakana
    ("ガ\u309b", "ｶ\uff9e\uff9e"),
    ("ガ\u3099", "ｶ\uff9e\uff9e"),
    ("カ\u309b\u309b", "ｶ\uff9e\uff9e"),
    ("カ\u3099\u3099", "ｶ\uff9e\uff9e"),
    ("カ\u3099\u309b", "ｶ\uff9e\uff9e"),
    ("カ\u309b\u3099", "ｶ\uff9e\uff9e"),
    ("パ\u309c", "ﾊ\uff9f\uff9f"),
    ("パ\u309a", "ﾊ\uff9f\uff9f"),
    ("ハ\u309c\u309c", "ﾊ\uff9f\uff9f"),
    ("ハ\u309a\u309a", "ﾊ\uff9f\uff9f"),
    ("ハ\u309a\u309c", "ﾊ\uff9f\uff9f"),
    ("ハ\u309c\u309a", "ﾊ\uff9f\uff9f"),
    # Voiced and semi-voiced sound marks not following katakana
    ("が\u309b", "が\u309b"),
    ("が\u3099", "が\u3099"),
    ("か\u309b\u309b", "か\u309b\u309b"),
    ("か\u3099\u3099", "か\u3099\u3099"),
    ("か\u3099\u309b", "か\u3099\u309b"),
    ("か\u309b\u3099", "か\u309b\u3099"),
    ("ぱ\u309c", "ぱ\u309c"),
    ("ぱ\u309a", "ぱ\u309a"),
    ("は\u309c\u309c", "は\u309c\u309c"),
    ("は\u309a\u309a", "は\u309a\u309a"),
    ("は\u309a\u309c", "は\u309a\u309c"),
    ("は\u309c\u309a", "は\u309c\u309a"),
    ("ｶ\uff9e\u309b", "ｶ\uff9e\u309b"),
    ("ｶ\uff9e\u3099", "ｶ\uff9e\u3099"),
    ("ﾊ\uff9f\u309c", "ﾊ\uff9f\u309c"),
    ("ﾊ\uff9f\u309a", "ﾊ\uff9f\u309a"),
    ("カ\u0000\u309b", "ｶ\u0000\u309b"),
    ("カ\u0000\u3099", "ｶ\u0000\u3099"),
    ("ハ\u0000\u309c", "ﾊ\u0000\u309c"),
    ("ハ\u0000\u309a", "ﾊ\u0000\u309a"),
    # Invalid variation selector following a convertible character
    ("ア\ufe00", "ｱ"),
    # Invalid variation selector not following a convertible character
    ("亜\ufe00", "亜\ufe00"),
]
FULL_TO_HALF_PUNCTUATION_CASES = [
    ("、", "､"),
    ("。", "｡"),
]
FULL_TO_HALF_CORNER_BRACKET_CASES = [
    ("「", "｢"),
    ("」", "｣"),
]
FULL_TO_HALF_CONJUNCTION_MARK_CASES = [
    ("・", "･"),
]
FULL_TO_HALF_LENGTH_MARK_CASES = [
    ("ー", "ｰ"),
]
FULL_TO_HALF_SPACE_CASES = [
    ("\u3000", "\u0020"),
]
FULL_TO_HALF_ASCII_SYMBOL_CASES = [
    ("！", "!"),
    ("＂", "\""),
    ("＃", "#"),
    ("＄", "$"),
    ("％", "%"),
    ("＆", "&"),
    ("＇", "'"),
    ("（", "("),
    ("）", ")"),
    ("＊", "*"),
    ("＋", "+"),
    ("，", ","),
    ("－", "-"),
    ("．", "."),
    ("／", "/"),
    ("：", ":"),
    ("；", ";"),
    ("＜", "<"),
    ("＝", "="),
    ("＞", ">"),
    ("？", "?"),
    ("＠", "@"),
    ("［", "["),
    ("＼", "\\"),
    ("］", "]"),
    ("＾", "^"),
    ("＿", "_"),
    ("｀", "`"),
    ("｛", "{"),
    ("｜", "|"),
    ("｝", "}"),
    ("\uff5e", "~"),
    ("｟", "｟"),
    ("｠", "｠"),
    ("！\ufe00", "!"),
    ("！\ufe01", "!"),
    ("，\ufe00", ","),
    ("，\ufe01", ","),
    ("．\ufe00", "."),
    ("．\ufe01", "."),
    ("：\ufe00", ":"),
    ("：\ufe01", ":"),
    ("；\ufe00", ";"),
    ("；\ufe01", ";"),
    ("？\ufe00", "?"),
    ("？\ufe01", "?"),
]
FULL_TO_HALF_ASCII_DIGIT_CASES = [
    ("０", "0"),
    ("１", "1"),
    ("２", "2"),
    ("３", "3"),
    ("４", "4"),
    ("５", "5"),
    ("６", "6"),
    ("７", "7"),
    ("８", "8"),
    ("９", "9"),
    ("０\ufe00", "0\ufe00"),
]
FULL_TO_HALF_ASCII_ALPHABET_CASES = [
    ("Ａ", "A"),
    ("Ｂ", "B"),
    ("Ｃ", "C"),
    ("Ｄ", "D"),
    ("Ｅ", "E"),
    ("Ｆ", "F"),
    ("Ｇ", "G"),
    ("Ｈ", "H"),
    ("Ｉ", "I"),
    ("Ｊ", "J"),
    ("Ｋ", "K"),
    ("Ｌ", "L"),
    ("Ｍ", "M"),
    ("Ｎ", "N"),
    ("Ｏ", "O"),
    ("Ｐ", "P"),
    ("Ｑ", "Q"),
    ("Ｒ", "R"),
    ("Ｓ", "S"),
    ("Ｔ", "T"),
    ("Ｕ", "U"),
    ("Ｖ", "V"),
    ("Ｗ", "W"),
    ("Ｘ", "X"),
    ("Ｙ", "Y"),
    ("Ｚ", "Z"),
    ("ａ", "a"),
    ("ｂ", "b"),
    ("ｃ", "c"),
    ("ｄ", "d"),
    ("ｅ", "e"),
    ("ｆ", "f"),
    ("ｇ", "g"),
    ("ｈ", "h"),
    ("ｉ", "i"),
    ("ｊ", "j"),
    ("ｋ", "k"),
    ("ｌ", "l"),
    ("ｍ", "m"),
    ("ｎ", "n"),
    ("ｏ", "o"),
    ("ｐ", "p"),
    ("ｑ", "q"),
    ("ｒ", "r"),
    ("ｓ", "s"),
    ("ｔ", "t"),
    ("ｕ", "u"),
    ("ｖ", "v"),
    ("ｗ", "w"),
    ("ｘ", "x"),
    ("ｙ", "y"),
    ("ｚ", "z"),
]
FULL_TO_HALF_WAVE_DASH_CASES = [
    ("\u301c", "~"),
]
FULL_TO_HALF_DEFAULT_CASES = (
    FULL_TO_HALF_BASE_CASES
    + FULL_TO_HALF_PUNCTUATION_CASES
    + FULL_TO_HALF_CORNER_BRACKET_CASES
    + FULL_TO_HALF_CONJUNCTION_MARK_CASES
    + FULL_TO_HALF_LENGTH_MARK_CASES
    + FULL_TO_HALF_SPACE_CASES
    + FULL_TO_HALF_ASCII_SYMBOL_CASES
    + FULL_TO_HALF_ASCII_DIGIT_CASES
    + FULL_TO_HALF_ASCII_ALPHABET_CASES
    + [(s, s) for (s, _) in FULL_TO_HALF_WAVE_DASH_CASES]
)


class TestFullToHalfConverter:
    """
    Tests for the FullToHalfConverter class.
    """

    @pytest.mark.parametrize("s,expect", FULL_TO_HALF_DEFAULT_CASES)
    # pylint: disable=W0613
    def test_convert(self, s, expect):
        """
        Verify default full-width to half-width conversion behavior.
        """
        cnv = FullToHalfConverter()
        actual = cnv.convert(s)
        assert actual == expect

    @pytest.mark.parametrize("s", [s for s, _ in FULL_TO_HALF_PUNCTUATION_CASES])
    def test_convert_without_punctuation(self, s):
        """
        Verify that punctuation conversion can be disabled.
        """
        cnv = FullToHalfConverter(
            WidthConverterConfig(punctuation=False),
        )
        actual = cnv.convert(s)
        assert actual == s

    @pytest.mark.parametrize("s", [s for s, _ in FULL_TO_HALF_CORNER_BRACKET_CASES])
    def test_convert_without_corner_brucket(self, s):
        """
        Verify that corner bracket conversion can be disabled.
        """
        cnv = FullToHalfConverter(
            WidthConverterConfig(corner_brucket=False),
        )
        actual = cnv.convert(s)
        assert actual == s

    @pytest.mark.parametrize("s", [s for s, _ in FULL_TO_HALF_CONJUNCTION_MARK_CASES])
    def test_convert_without_conjunction_mark(self, s):
        """
        Verify that conjunction mark conversion can be disabled.
        """
        cnv = FullToHalfConverter(
            WidthConverterConfig(conjunction_mark=False),
        )
        actual = cnv.convert(s)
        assert actual == s

    @pytest.mark.parametrize("s", [s for s, _ in FULL_TO_HALF_LENGTH_MARK_CASES])
    def test_convert_without_length_mark(self, s):
        """
        Verify that length mark conversion can be disabled.
        """
        cnv = FullToHalfConverter(
            WidthConverterConfig(length_mark=False),
        )
        actual = cnv.convert(s)
        assert actual == s

    @pytest.mark.parametrize("s", [s for s, _ in FULL_TO_HALF_SPACE_CASES])
    def test_convert_without_space(self, s):
        """
        Verify that space conversion can be disabled.
        """
        cnv = FullToHalfConverter(
            WidthConverterConfig(space=False),
        )
        actual = cnv.convert(s)
        assert actual == s

    @pytest.mark.parametrize("s", [s for s, _ in FULL_TO_HALF_ASCII_SYMBOL_CASES])
    def test_convert_without_ascii_symbol(self, s):
        """
        Verify that ASCII symbol conversion can be disabled.
        """
        cnv = FullToHalfConverter(
            WidthConverterConfig(ascii_symbol=False),
        )
        actual = cnv.convert(s)
        assert actual == s

    @pytest.mark.parametrize("s", [s for s, _ in FULL_TO_HALF_ASCII_DIGIT_CASES])
    def test_convert_without_ascii_digit(self, s):
        """
        Verify that ASCII digit conversion can be disabled.
        """
        cnv = FullToHalfConverter(
            WidthConverterConfig(ascii_digit=False),
        )
        actual = cnv.convert(s)
        assert actual == s

    @pytest.mark.parametrize("s", [s for s, _ in FULL_TO_HALF_ASCII_ALPHABET_CASES])
    def test_convert_without_ascii_alphabet(self, s):
        """
        Verify that ASCII alphabet conversion can be disabled.
        """
        cnv = FullToHalfConverter(
            WidthConverterConfig(ascii_alphabet=False),
        )
        actual = cnv.convert(s)
        assert actual == s

    @pytest.mark.parametrize("s,expect", FULL_TO_HALF_WAVE_DASH_CASES)
    def test_convert_with_wave_dash(self, s, expect):
        """
        Verify that wave dash conversion can be enabled.
        """
        cnv = FullToHalfConverter(
            WidthConverterConfig(wave_dash=True),
        )
        actual = cnv.convert(s)
        assert actual == expect

    def test_convert_with_invalid_parameter(self):
        """
        Verify that non-string input raises a TypeError.
        """
        cnv = FullToHalfConverter()

        with pytest.raises(TypeError, match="s must be a string."):
            cnv.convert(None)  # type: ignore
