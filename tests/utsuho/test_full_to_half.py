import pytest

from utsuho import ConverterConfig, FullToHalfConverter


@pytest.mark.parametrize('s,expect', [
    ('ア', 'ｱ'), ('イ', 'ｲ'), ('ウ', 'ｳ'), ('エ', 'ｴ'), ('オ', 'ｵ'),
    ('カ', 'ｶ'), ('キ', 'ｷ'), ('ク', 'ｸ'), ('ケ', 'ｹ'), ('コ', 'ｺ'),
    ('サ', 'ｻ'), ('シ', 'ｼ'), ('ス', 'ｽ'), ('セ', 'ｾ'), ('ソ', 'ｿ'),
    ('タ', 'ﾀ'), ('チ', 'ﾁ'), ('ツ', 'ﾂ'), ('テ', 'ﾃ'), ('ト', 'ﾄ'),
    ('ナ', 'ﾅ'), ('ニ', 'ﾆ'), ('ヌ', 'ﾇ'), ('ネ', 'ﾈ'), ('ノ', 'ﾉ'),
    ('ハ', 'ﾊ'), ('ヒ', 'ﾋ'), ('フ', 'ﾌ'), ('ヘ', 'ﾍ'), ('ホ', 'ﾎ'),
    ('マ', 'ﾏ'), ('ミ', 'ﾐ'), ('ム', 'ﾑ'), ('メ', 'ﾒ'), ('モ', 'ﾓ'),
    ('ヤ', 'ﾔ'), ('ユ', 'ﾕ'), ('ヨ', 'ﾖ'),
    ('ラ', 'ﾗ'), ('リ', 'ﾘ'), ('ル', 'ﾙ'), ('レ', 'ﾚ'), ('ロ', 'ﾛ'),
    ('ワ', 'ﾜ'), ('ヲ', 'ｦ'), ('ン', 'ﾝ'),
    ('ャ', 'ｬ'), ('ュ', 'ｭ'), ('ョ', 'ｮ'), ('ッ', 'ｯ'),
    ('ァ', 'ｧ'), ('ィ', 'ｨ'), ('ゥ', 'ｩ'), ('ェ', 'ｪ'), ('ォ', 'ｫ'),
    ('ガ', 'ｶﾞ'), ('ギ', 'ｷﾞ'), ('グ', 'ｸﾞ'), ('ゲ', 'ｹﾞ'), ('ゴ', 'ｺﾞ'),
    ('ザ', 'ｻﾞ'), ('ジ', 'ｼﾞ'), ('ズ', 'ｽﾞ'), ('ゼ', 'ｾﾞ'), ('ゾ', 'ｿﾞ'),
    ('ダ', 'ﾀﾞ'), ('ヂ', 'ﾁﾞ'), ('ヅ', 'ﾂﾞ'), ('デ', 'ﾃﾞ'), ('ド', 'ﾄﾞ'),
    ('バ', 'ﾊﾞ'), ('ビ', 'ﾋﾞ'), ('ブ', 'ﾌﾞ'), ('ベ', 'ﾍﾞ'), ('ボ', 'ﾎﾞ'),
    ('パ', 'ﾊﾟ'), ('ピ', 'ﾋﾟ'), ('プ', 'ﾌﾟ'), ('ペ', 'ﾍﾟ'), ('ポ', 'ﾎﾟ'),
    ('ヴ', 'ｳﾞ'), ('ヷ', 'ﾜﾞ'), ('ヺ', 'ｦﾞ'),
    ('カ\u3099', 'ｶﾞ'), ('キ\u3099', 'ｷﾞ'), ('ク\u3099', 'ｸﾞ'), ('ケ\u3099', 'ｹﾞ'), ('コ\u3099', 'ｺﾞ'),
    ('サ\u3099', 'ｻﾞ'), ('シ\u3099', 'ｼﾞ'), ('ス\u3099', 'ｽﾞ'), ('セ\u3099', 'ｾﾞ'), ('ソ\u3099', 'ｿﾞ'),
    ('タ\u3099', 'ﾀﾞ'), ('チ\u3099', 'ﾁﾞ'), ('ツ\u3099', 'ﾂﾞ'), ('テ\u3099', 'ﾃﾞ'), ('ト\u3099', 'ﾄﾞ'),
    ('ハ\u3099', 'ﾊﾞ'), ('ヒ\u3099', 'ﾋﾞ'), ('フ\u3099', 'ﾌﾞ'), ('ヘ\u3099', 'ﾍﾞ'), ('ホ\u3099', 'ﾎﾞ'),
    ('ハ\u309A', 'ﾊﾟ'), ('ヒ\u309A', 'ﾋﾟ'), ('フ\u309A', 'ﾌﾟ'), ('ヘ\u309A', 'ﾍﾟ'), ('ホ\u309A', 'ﾎﾟ'),
    ('ウ\u3099', 'ｳﾞ'), ('ワ\u3099', 'ﾜﾞ'), ('ヲ\u3099', 'ｦﾞ'),
    ('ー', 'ｰ'), ('・', '･'),
    ('。', '｡'), ('、', '､'), ('「', '｢'), ('」', '｣'),
    ('ア\u3099', 'ｱ\uFF9E'), ('ア\u309A', 'ｱ\uFF9F'), ('ア゛', 'ｱ\uFF9E'), ('ア゜', 'ｱ\uFF9F'),
    ('ガ゛', 'ｶﾞﾞ'), ('ア゛゛', 'ｱﾞﾞ'), ('ム゛', 'ﾑﾞ'),
    ('パ゜', 'ﾊﾟﾟ'), ('ア゜゜', 'ｱﾟﾟ'), ('ム゜', 'ﾑﾟ'),
    ('゛ダ\u3099た\u3099゛ダ゛', '゛ﾀﾞﾞた\u3099゛ﾀﾞﾞ'),
])
def test_full_to_half(s, expect):
    cnv = FullToHalfConverter()
    actual = cnv.convert(s)
    assert actual == expect

    config = ConverterConfig(punctuation=False)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    if s == '。' or s == '、':
        assert actual == s
    else:
        assert actual == expect

    config = ConverterConfig(corner_brucket=False)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    if s == '「' or s == '」':
        assert actual == s
    else:
        assert actual == expect

    config = ConverterConfig(conjunction_mark=False)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    if s == '・':
        assert actual == s
    else:
        assert actual == expect

    config = ConverterConfig(length_mark=False)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    if s == 'ー':
        assert actual == s
    else:
        assert actual == expect


def test_full_to_half_with_controls():
    s = '\u30BF\u0000\u309B'
    cnv = FullToHalfConverter()
    actual = cnv.convert(s)
    print([ord(c) for c in s])
    print([ord(c) for c in actual])
    assert actual == '\uFF80\u0000\u309B'


def test_full_to_half_invalid_parameter():
    cnv = FullToHalfConverter()

    with pytest.raises(TypeError, match='s must be a string.') as exc:
        cnv.convert(None)
