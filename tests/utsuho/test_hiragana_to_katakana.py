"""
Tests for the HiraganaToKatakanaConverter class.
"""

import pytest

from utsuho.converters import HiraganaToKatakanaConverter

HIRA_TO_KATA_DEFAULT_CASES = [
    # Hiragana (unvoiced)
    ("あ", "ア"),
    ("い", "イ"),
    ("う", "ウ"),
    ("え", "エ"),
    ("お", "オ"),
    ("か", "カ"),
    ("き", "キ"),
    ("く", "ク"),
    ("け", "ケ"),
    ("こ", "コ"),
    ("さ", "サ"),
    ("し", "シ"),
    ("す", "ス"),
    ("せ", "セ"),
    ("そ", "ソ"),
    ("た", "タ"),
    ("ち", "チ"),
    ("つ", "ツ"),
    ("て", "テ"),
    ("と", "ト"),
    ("な", "ナ"),
    ("に", "ニ"),
    ("ぬ", "ヌ"),
    ("ね", "ネ"),
    ("の", "ノ"),
    ("は", "ハ"),
    ("ひ", "ヒ"),
    ("ふ", "フ"),
    ("へ", "ヘ"),
    ("ほ", "ホ"),
    ("ま", "マ"),
    ("み", "ミ"),
    ("む", "ム"),
    ("め", "メ"),
    ("も", "モ"),
    ("や", "ヤ"),
    ("ゆ", "ユ"),
    ("よ", "ヨ"),
    ("ら", "ラ"),
    ("り", "リ"),
    ("る", "ル"),
    ("れ", "レ"),
    ("ろ", "ロ"),
    ("わ", "ワ"),
    ("ゐ", "ヰ"),
    ("ゑ", "ヱ"),
    ("を", "ヲ"),
    ("ん", "ン"),
    # Hiragana (unvoiced, small)
    ("ぁ", "ァ"),
    ("ぃ", "ィ"),
    ("ぅ", "ゥ"),
    ("ぇ", "ェ"),
    ("ぉ", "ォ"),
    ("っ", "ッ"),
    ("ゃ", "ャ"),
    ("ゅ", "ュ"),
    ("ょ", "ョ"),
    ("ゎ", "ヮ"),
    ("ゕ", "ヵ"),
    ("ゖ", "ヶ"),
    # Hiragana (voiced)
    ("が", "ガ"),
    ("ぎ", "ギ"),
    ("ぐ", "グ"),
    ("げ", "ゲ"),
    ("ご", "ゴ"),
    ("ざ", "ザ"),
    ("じ", "ジ"),
    ("ず", "ズ"),
    ("ぜ", "ゼ"),
    ("ぞ", "ゾ"),
    ("だ", "ダ"),
    ("ぢ", "ヂ"),
    ("づ", "ヅ"),
    ("で", "デ"),
    ("ど", "ド"),
    ("ば", "バ"),
    ("び", "ビ"),
    ("ぶ", "ブ"),
    ("べ", "ベ"),
    ("ぼ", "ボ"),
    ("ゔ", "ヴ"),
    # Hiragana (semi-voiced)
    ("ぱ", "パ"),
    ("ぴ", "ピ"),
    ("ぷ", "プ"),
    ("ぺ", "ペ"),
    ("ぽ", "ポ"),
    # Hiragana (voiced and semi-voiced sound marks)
    ("\u309b", "\u309b"),
    ("\u309c", "\u309c"),
    # Katakana (middle dot and long vowel mark)
    ("・", "・"),
    ("ー", "ー"),
    # Hiragana (other)
    ("ゝ", "ヽ"),
    ("ゞ", "ヾ"),
    ("ゟ", "ゟ"),
]


class TestHiraganaToKatakanaConverter:
    """
    Tests for the HiraganaToKatakanaConverter class.
    """

    @pytest.mark.parametrize("s,expect", HIRA_TO_KATA_DEFAULT_CASES)
    def test_convert(self, s, expect):
        """
        Verify hiragana to katakana conversion behavior.
        """
        cnv = HiraganaToKatakanaConverter()
        actual = cnv.convert(s)
        assert actual == expect

    def test_convert_with_invalid_parameter(self):
        """
        Verify that non-string input raises a TypeError.
        """
        cnv = HiraganaToKatakanaConverter()

        with pytest.raises(TypeError, match="s must be a string."):
            cnv.convert(None)  # type: ignore
