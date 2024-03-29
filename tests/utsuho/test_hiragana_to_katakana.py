import pytest

from utsuho.converters import HiraganaToKatakanaConverter

test_data = [
    # ひらがな (清音)
    ('あ', 'ア'), ('い', 'イ'), ('う', 'ウ'), ('え', 'エ'), ('お', 'オ'),
    ('か', 'カ'), ('き', 'キ'), ('く', 'ク'), ('け', 'ケ'), ('こ', 'コ'),
    ('さ', 'サ'), ('し', 'シ'), ('す', 'ス'), ('せ', 'セ'), ('そ', 'ソ'),
    ('た', 'タ'), ('ち', 'チ'), ('つ', 'ツ'), ('て', 'テ'), ('と', 'ト'),
    ('な', 'ナ'), ('に', 'ニ'), ('ぬ', 'ヌ'), ('ね', 'ネ'), ('の', 'ノ'),
    ('は', 'ハ'), ('ひ', 'ヒ'), ('ふ', 'フ'), ('へ', 'ヘ'), ('ほ', 'ホ'),
    ('ま', 'マ'), ('み', 'ミ'), ('む', 'ム'), ('め', 'メ'), ('も', 'モ'),
    ('や', 'ヤ'), ('ゆ', 'ユ'), ('よ', 'ヨ'),
    ('ら', 'ラ'), ('り', 'リ'), ('る', 'ル'), ('れ', 'レ'), ('ろ', 'ロ'),
    ('わ', 'ワ'), ('ゐ', 'ヰ'), ('ゑ', 'ヱ'),
    ('を', 'ヲ'), ('ん', 'ン'),
    # ひらがな (清音 [小書])
    ('ぁ', 'ァ'), ('ぃ', 'ィ'), ('ぅ', 'ゥ'), ('ぇ', 'ェ'), ('ぉ', 'ォ'),
    ('っ', 'ッ'), ('ゃ', 'ャ'), ('ゅ', 'ュ'), ('ょ', 'ョ'),
    ('ゎ', 'ヮ'), ('ゕ', 'ヵ'), ('ゖ', 'ヶ'),
    # ひらがな (濁音)
    ('が', 'ガ'), ('ぎ', 'ギ'), ('ぐ', 'グ'), ('げ', 'ゲ'), ('ご', 'ゴ'),
    ('ざ', 'ザ'), ('じ', 'ジ'), ('ず', 'ズ'), ('ぜ', 'ゼ'), ('ぞ', 'ゾ'),
    ('だ', 'ダ'), ('ぢ', 'ヂ'), ('づ', 'ヅ'), ('で', 'デ'), ('ど', 'ド'),
    ('ば', 'バ'), ('び', 'ビ'), ('ぶ', 'ブ'), ('べ', 'ベ'), ('ぼ', 'ボ'),
    ('ゔ', 'ヴ'),
    # ひらがな (半濁音)
    ('ぱ', 'パ'), ('ぴ', 'ピ'), ('ぷ', 'プ'), ('ぺ', 'ペ'), ('ぽ', 'ポ'),
    # ひらがな (濁音・半濁音記号)
    ('\u309B', '\u309B'), ('\u309C', '\u309C'),
    # カタカナ (中黒・長音記号)
    ('・', '・'), ('ー', 'ー'),
    # ひらがな (その他)
    ('ゝ', 'ヽ'), ('ゞ', 'ヾ'), ('ゟ', 'ゟ'),
]


@pytest.mark.parametrize('s,expect', test_data)
def test_hiragana_to_katakana(s, expect):
    cnv = HiraganaToKatakanaConverter()
    actual = cnv.convert(s)

    assert actual == expect


def test_hiragana_to_katakana_with_invalid_parameter():
    cnv = HiraganaToKatakanaConverter()

    with pytest.raises(TypeError, match='s must be a string.') as exc:
        cnv.convert(None)
