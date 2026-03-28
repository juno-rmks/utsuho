"""
Tests for the KatakanaToHiraganaConverter class.
"""

import pytest

from utsuho.converters import KatakanaToHiraganaConverter

KATA_TO_HIRA_DEFAULT_CASES = [
    # Katakana (unvoiced)
    ("ア", "あ"),
    ("イ", "い"),
    ("ウ", "う"),
    ("エ", "え"),
    ("オ", "お"),
    ("カ", "か"),
    ("キ", "き"),
    ("ク", "く"),
    ("ケ", "け"),
    ("コ", "こ"),
    ("サ", "さ"),
    ("シ", "し"),
    ("ス", "す"),
    ("セ", "せ"),
    ("ソ", "そ"),
    ("タ", "た"),
    ("チ", "ち"),
    ("ツ", "つ"),
    ("テ", "て"),
    ("ト", "と"),
    ("ナ", "な"),
    ("ニ", "に"),
    ("ヌ", "ぬ"),
    ("ネ", "ね"),
    ("ノ", "の"),
    ("ハ", "は"),
    ("ヒ", "ひ"),
    ("フ", "ふ"),
    ("ヘ", "へ"),
    ("ホ", "ほ"),
    ("マ", "ま"),
    ("ミ", "み"),
    ("ム", "む"),
    ("メ", "め"),
    ("モ", "も"),
    ("ヤ", "や"),
    ("ユ", "ゆ"),
    ("ヨ", "よ"),
    ("ラ", "ら"),
    ("リ", "り"),
    ("ル", "る"),
    ("レ", "れ"),
    ("ロ", "ろ"),
    ("ワ", "わ"),
    ("ヰ", "ゐ"),
    ("ヱ", "ゑ"),
    ("ヲ", "を"),
    ("ン", "ん"),
    # Katakana (unvoiced, small)
    ("ァ", "ぁ"),
    ("ィ", "ぃ"),
    ("ゥ", "ぅ"),
    ("ェ", "ぇ"),
    ("ォ", "ぉ"),
    ("ッ", "っ"),
    ("ャ", "ゃ"),
    ("ュ", "ゅ"),
    ("ョ", "ょ"),
    ("ヮ", "ゎ"),
    ("ヵ", "ゕ"),
    ("ヶ", "ゖ"),
    # Katakana (voiced)
    ("ガ", "が"),
    ("ギ", "ぎ"),
    ("グ", "ぐ"),
    ("ゲ", "げ"),
    ("ゴ", "ご"),
    ("ザ", "ざ"),
    ("ジ", "じ"),
    ("ズ", "ず"),
    ("ゼ", "ぜ"),
    ("ゾ", "ぞ"),
    ("ダ", "だ"),
    ("ヂ", "ぢ"),
    ("ヅ", "づ"),
    ("デ", "で"),
    ("ド", "ど"),
    ("バ", "ば"),
    ("ビ", "び"),
    ("ブ", "ぶ"),
    ("ベ", "べ"),
    ("ボ", "ぼ"),
    ("ヷ", "ヷ"),
    ("ヸ", "ヸ"),
    ("ヴ", "ゔ"),
    ("ヹ", "ヹ"),
    ("ヺ", "ヺ"),
    # Katakana (semi-voiced)
    ("パ", "ぱ"),
    ("ピ", "ぴ"),
    ("プ", "ぷ"),
    ("ペ", "ぺ"),
    ("ポ", "ぽ"),
    # Hiragana (voiced and semi-voiced sound marks)
    ("\u309b", "\u309b"),
    ("\u309c", "\u309c"),
    # Katakana (middle dot and long vowel mark)
    ("・", "・"),
    ("ー", "ー"),
    # Katakana (other)
    ("゠", "゠"),
    ("ヽ", "ゝ"),
    ("ヾ", "ゞ"),
    ("ヿ", "ヿ"),
]


class TestKatakanaToHiraganaConverter:
    """
    Tests for the KatakanaToHiraganaConverter class.
    """

    @pytest.mark.parametrize("s,expect", KATA_TO_HIRA_DEFAULT_CASES)
    def test_convert(self, s, expect):
        """
        Verify katakana to hiragana conversion behavior.
        """
        cnv = KatakanaToHiraganaConverter()
        actual = cnv.convert(s)
        assert actual == expect

    def test_convert_with_invalid_parameter(self):
        """
        Verify that non-string input raises a TypeError.
        """
        cnv = KatakanaToHiraganaConverter()

        with pytest.raises(TypeError, match="s must be a string."):
            cnv.convert(None)  # type: ignore
