import pytest

from utsuho import ConverterConfig, HalfToFullConverter


@pytest.mark.parametrize('s,expect', [
    ('ｱ', 'ア'), ('ｲ', 'イ'), ('ｳ', 'ウ'), ('ｴ', 'エ'), ('ｵ', 'オ'),
    ('ｶ', 'カ'), ('ｷ', 'キ'), ('ｸ', 'ク'), ('ｹ', 'ケ'), ('ｺ', 'コ'),
    ('ｻ', 'サ'), ('ｼ', 'シ'), ('ｽ', 'ス'), ('ｾ', 'セ'), ('ｿ', 'ソ'),
    ('ﾀ', 'タ'), ('ﾁ', 'チ'), ('ﾂ', 'ツ'), ('ﾃ', 'テ'), ('ﾄ', 'ト'),
    ('ﾅ', 'ナ'), ('ﾆ', 'ニ'), ('ﾇ', 'ヌ'), ('ﾈ', 'ネ'), ('ﾉ', 'ノ'),
    ('ﾊ', 'ハ'), ('ﾋ', 'ヒ'), ('ﾌ', 'フ'), ('ﾍ', 'ヘ'), ('ﾎ', 'ホ'),
    ('ﾏ', 'マ'), ('ﾐ', 'ミ'), ('ﾑ', 'ム'), ('ﾒ', 'メ'), ('ﾓ', 'モ'),
    ('ﾔ', 'ヤ'), ('ﾕ', 'ユ'), ('ﾖ', 'ヨ'),
    ('ﾗ', 'ラ'), ('ﾘ', 'リ'), ('ﾙ', 'ル'), ('ﾚ', 'レ'), ('ﾛ', 'ロ'),
    ('ﾜ', 'ワ'), ('ｦ', 'ヲ'), ('ﾝ', 'ン'),
    ('ｬ', 'ャ'), ('ｭ', 'ュ'), ('ｮ', 'ョ'), ('ｯ', 'ッ'),
    ('ｧ', 'ァ'), ('ｨ', 'ィ'), ('ｩ', 'ゥ'), ('ｪ', 'ェ'), ('ｫ', 'ォ'),
    ('ｶﾞ', 'ガ'), ('ｷﾞ', 'ギ'), ('ｸﾞ', 'グ'), ('ｹﾞ', 'ゲ'), ('ｺﾞ', 'ゴ'),
    ('ｻﾞ', 'ザ'), ('ｼﾞ', 'ジ'), ('ｽﾞ', 'ズ'), ('ｾﾞ', 'ゼ'), ('ｿﾞ', 'ゾ'),
    ('ﾀﾞ', 'ダ'), ('ﾁﾞ', 'ヂ'), ('ﾂﾞ', 'ヅ'), ('ﾃﾞ', 'デ'), ('ﾄﾞ', 'ド'),
    ('ﾊﾞ', 'バ'), ('ﾋﾞ', 'ビ'), ('ﾌﾞ', 'ブ'), ('ﾍﾞ', 'ベ'), ('ﾎﾞ', 'ボ'),
    ('ﾊﾟ', 'パ'), ('ﾋﾟ', 'ピ'), ('ﾌﾟ', 'プ'), ('ﾍﾟ', 'ペ'), ('ﾎﾟ', 'ポ'),
    ('ｳﾞ', 'ヴ'), ('ﾜﾞ', 'ヷ'), ('ｦﾞ', 'ヺ'),
    ('ｰ', 'ー'), ('･', '・'),
    ('｡', '。'), ('､', '、'), ('｢', '「'), ('｣', '」'),
    ('\uFF9E', '゛'), ('\uFF9F', '゜'),
    ('ｶﾞﾞ', 'ガ゛'), ('ﾞﾞ', '゛゛'), ('ﾑﾞ', 'ム゛'),
    ('ﾊﾟﾟ', 'パ゜'), ('ﾟﾟ', '゜゜'), ('ﾑﾟ', 'ム゜'),
    ('｢AｱｶﾞB漢｣', '「AアガB漢」'), ('「ＡアガＢ漢」', '「ＡアガＢ漢」'),
])
def test_half_to_full(s, expect):
    cnv = HalfToFullConverter()
    actual = cnv.convert(s)
    assert actual == expect

    config = ConverterConfig(punctuation=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    if s == '｡' or s == '､':
        assert actual == s
    else:
        assert actual == expect

    config = ConverterConfig(corner_brucket=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    if s == '｢' or s == '｣':
        assert actual == s
    elif s == '｢AｱｶﾞB漢｣':
        assert actual == '｢AアガB漢｣'
    else:
        assert actual == expect

    config = ConverterConfig(conjunction_mark=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    if s == '･':
        assert actual == s
    else:
        assert actual == expect

    config = ConverterConfig(length_mark=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    if s == 'ｰ':
        assert actual == s
    else:
        assert actual == expect


def test_half_to_full_invalid_parameter():
    cnv = HalfToFullConverter()

    with pytest.raises(TypeError, match='s must be a string.') as exc:
        cnv.convert(None)
