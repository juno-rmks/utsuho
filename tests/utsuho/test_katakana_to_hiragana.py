import pytest

from utsuho.converters import KatakanaToHiraganaConverter

test_data = [
    # カタカナ (清音)
    ('ア', 'あ'), ('イ', 'い'), ('ウ', 'う'), ('エ', 'え'), ('オ', 'お'),
    ('カ', 'か'), ('キ', 'き'), ('ク', 'く'), ('ケ', 'け'), ('コ', 'こ'),
    ('サ', 'さ'), ('シ', 'し'), ('ス', 'す'), ('セ', 'せ'), ('ソ', 'そ'),
    ('タ', 'た'), ('チ', 'ち'), ('ツ', 'つ'), ('テ', 'て'), ('ト', 'と'),
    ('ナ', 'な'), ('ニ', 'に'), ('ヌ', 'ぬ'), ('ネ', 'ね'), ('ノ', 'の'),
    ('ハ', 'は'), ('ヒ', 'ひ'), ('フ', 'ふ'), ('ヘ', 'へ'), ('ホ', 'ほ'),
    ('マ', 'ま'), ('ミ', 'み'), ('ム', 'む'), ('メ', 'め'), ('モ', 'も'),
    ('ヤ', 'や'), ('ユ', 'ゆ'), ('ヨ', 'よ'),
    ('ラ', 'ら'), ('リ', 'り'), ('ル', 'る'), ('レ', 'れ'), ('ロ', 'ろ'),
    ('ワ', 'わ'), ('ヰ', 'ゐ'), ('ヱ', 'ゑ'),
    ('ヲ', 'を'), ('ン', 'ん'),
    # カタカナ (清音 [小書])
    ('ァ', 'ぁ'), ('ィ', 'ぃ'), ('ゥ', 'ぅ'), ('ェ', 'ぇ'), ('ォ', 'ぉ'),
    ('ッ', 'っ'), ('ャ', 'ゃ'), ('ュ', 'ゅ'), ('ョ', 'ょ'),
    ('ヮ', 'ゎ'), ('ヵ', 'ゕ'), ('ヶ', 'ゖ'),
    # カタカナ (濁音)
    ('ガ', 'が'), ('ギ', 'ぎ'), ('グ', 'ぐ'), ('ゲ', 'げ'), ('ゴ', 'ご'),
    ('ザ', 'ざ'), ('ジ', 'じ'), ('ズ', 'ず'), ('ゼ', 'ぜ'), ('ゾ', 'ぞ'),
    ('ダ', 'だ'), ('ヂ', 'ぢ'), ('ヅ', 'づ'), ('デ', 'で'), ('ド', 'ど'),
    ('バ', 'ば'), ('ビ', 'び'), ('ブ', 'ぶ'), ('ベ', 'べ'), ('ボ', 'ぼ'),
    ('ヷ', 'ヷ'), ('ヸ', 'ヸ'), ('ヴ', 'ゔ'), ('ヹ', 'ヹ'), ('ヺ', 'ヺ'),
    # カタカナ (半濁音)
    ('パ', 'ぱ'), ('ピ', 'ぴ'), ('プ', 'ぷ'), ('ペ', 'ぺ'), ('ポ', 'ぽ'),
    # ひらがな (濁音・半濁音記号)
    ('\u309B', '\u309B'), ('\u309C', '\u309C'),
    # カタカナ (中黒・長音記号)
    ('・', '・'), ('ー', 'ー'),
    # カタカナ (その他)
    ('゠', '゠'), ('ヽ', 'ゝ'), ('ヾ', 'ゞ'), ('ヿ', 'ヿ'),
]


@pytest.mark.parametrize('s,expect', test_data)
def test_katakana_to_hiragana(s, expect):
    cnv = KatakanaToHiraganaConverter()
    actual = cnv.convert(s)

    assert actual == expect


def test_katakana_to_hiragana_with_invalid_parameter():
    cnv = KatakanaToHiraganaConverter()

    with pytest.raises(TypeError, match='s must be a string.') as exc:
        cnv.convert(None)
