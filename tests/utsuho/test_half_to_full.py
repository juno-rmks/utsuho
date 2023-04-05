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
    ('｢AｱｶﾞB漢｣', '「ＡアガＢ漢」'), ('「ＡアガＢ漢」', '「ＡアガＢ漢」'),
    ('0', '０'), ('1', '１'), ('2', '２'), ('3', '３'), ('4', '４'),
    ('5', '５'), ('6', '６'), ('7', '７'), ('8', '８'), ('9', '９'),
    ('0\uFE00', '０\uFE00'), ('\uFE001\uFE00', '\uFE00１'),
    ('A', 'Ａ'), ('B', 'Ｂ'), ('C', 'Ｃ'), ('D', 'Ｄ'), ('E', 'Ｅ'),
    ('F', 'Ｆ'), ('G', 'Ｇ'), ('H', 'Ｈ'), ('I', 'Ｉ'), ('J', 'Ｊ'),
    ('K', 'Ｋ'), ('L', 'Ｌ'), ('M', 'Ｍ'), ('N', 'Ｎ'), ('O', 'Ｏ'),
    ('P', 'Ｐ'), ('Q', 'Ｑ'), ('R', 'Ｒ'), ('S', 'Ｓ'), ('T', 'Ｔ'),
    ('U', 'Ｕ'), ('V', 'Ｖ'), ('W', 'Ｗ'), ('X', 'Ｘ'), ('Y', 'Ｙ'),
    ('Z', 'Ｚ'),
    ('a', 'ａ'), ('b', 'ｂ'), ('c', 'ｃ'), ('d', 'ｄ'), ('e', 'ｅ'),
    ('f', 'ｆ'), ('g', 'ｇ'), ('h', 'ｈ'), ('i', 'ｉ'), ('j', 'ｊ'),
    ('k', 'ｋ'), ('l', 'ｌ'), ('m', 'ｍ'), ('n', 'ｎ'), ('o', 'ｏ'),
    ('p', 'ｐ'), ('q', 'ｑ'), ('r', 'ｒ'), ('s', 'ｓ'), ('t', 'ｔ'),
    ('u', 'ｕ'), ('v', 'ｖ'), ('w', 'ｗ'), ('x', 'ｘ'), ('y', 'ｙ'),
    ('z', 'ｚ'),
    ('!', '！'), ('"', '＂'), ('#', '＃'), ('$', '＄'), ('%', '％'),
    ('&', '＆'), ('\'', '＇'), ('(', '（'), (')', '）'), ('*', '＊'),
    ('+', '＋'), (',', '，'), ('-', '－'), ('.', '．'), ('/', '／'),
    (':', '：'), (';', '；'), ('<', '＜'), ('=', '＝'), ('>', '＞'),
    ('?', '？'), ('@', '＠'), ('[', '［'), ('\\', '＼'), (']', '］'),
    ('^', '＾'), ('_', '＿'), ('`', '｀'), ('{', '｛'), ('|', '｜'),
    ('}', '｝'), ('~', '～'),
    ('\u0020', '　'), ('\u00A0', '　'),
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
        assert actual == '｢ＡアガＢ漢｣'
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

    config = ConverterConfig(space=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    if s in ['\u0020', '\u00A0'] or s == '〜':
        assert actual == s
    else:
        assert actual == expect

    config = ConverterConfig(ascii_symbol=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    if s in [chr(c) for c in range(ord('!'), ord('/') + 1)] \
            or s in [chr(c) for c in range(ord(':'), ord('@') + 1)] \
            or s in [chr(c) for c in range(ord('['), ord('`') + 1)] \
            or s in [chr(c) for c in range(ord('{'), ord('~') + 1)]:
        assert actual == s
    else:
        assert actual == expect

    config = ConverterConfig(ascii_digit=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    if s in [chr(c) for c in range(ord('0'), ord('9') + 1)] or s == '0\uFE00' or s == '\uFE001\uFE00':
        assert actual == s
    else:
        assert actual == expect

    config = ConverterConfig(ascii_alphabet=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    if s in [chr(c) for c in range(ord('A'), ord('Z') + 1)] or s in [chr(c) for c in range(ord('a'), ord('z') + 1)]:
        assert actual == s
    elif s == '｢AｱｶﾞB漢｣':
        assert actual == '「AアガB漢」'
    else:
        assert actual == expect


def test_half_to_full_with_controls():
    s = '\uFF80\u0000\uFF9E'
    cnv = HalfToFullConverter()
    actual = cnv.convert(s)
    assert actual == '\u30BF\u0000\u309B'


def test_half_to_full_invalid_parameter():
    cnv = HalfToFullConverter()

    with pytest.raises(TypeError, match='s must be a string.') as exc:
        cnv.convert(None)
