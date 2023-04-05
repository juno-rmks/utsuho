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
    ('０', '0'), ('１', '1'), ('２', '2'), ('３', '3'), ('４', '4'),
    ('５', '5'), ('６', '6'), ('７', '7'), ('８', '8'), ('９', '9'),
    ('０\uFE00', '0\uFE00'), ('\uFE00１\uFE00', '\uFE001'),
    ('Ａ', 'A'), ('Ｂ', 'B'), ('Ｃ', 'C'), ('Ｄ', 'D'), ('Ｅ', 'E'),
    ('Ｆ', 'F'), ('Ｇ', 'G'), ('Ｈ', 'H'), ('Ｉ', 'I'), ('Ｊ', 'J'),
    ('Ｋ', 'K'), ('Ｌ', 'L'), ('Ｍ', 'M'), ('Ｎ', 'N'), ('Ｏ', 'O'),
    ('Ｐ', 'P'), ('Ｑ', 'Q'), ('Ｒ', 'R'), ('Ｓ', 'S'), ('Ｔ', 'T'),
    ('Ｕ', 'U'), ('Ｖ', 'V'), ('Ｗ', 'W'), ('Ｘ', 'X'), ('Ｙ', 'Y'),
    ('Ｚ', 'Z'),
    ('ａ', 'a'), ('ｂ', 'b'), ('ｃ', 'c'), ('ｄ', 'd'), ('ｅ', 'e'),
    ('ｆ', 'f'), ('ｇ', 'g'), ('ｈ', 'h'), ('ｉ', 'i'), ('ｊ', 'j'),
    ('ｋ', 'k'), ('ｌ', 'l'), ('ｍ', 'm'), ('ｎ', 'n'), ('ｏ', 'o'),
    ('ｐ', 'p'), ('ｑ', 'q'), ('ｒ', 'r'), ('ｓ', 's'), ('ｔ', 't'),
    ('ｕ', 'u'), ('ｖ', 'v'), ('ｗ', 'w'), ('ｘ', 'x'), ('ｙ', 'y'),
    ('ｚ', 'z'),
    ('！', '!'), ('＂', '"'), ('＃', '#'), ('＄', '$'), ('％', '%'),
    ('＆', '&'), ('＇', '\''), ('（', '('), ('）', ')'), ('＊', '*'),
    ('＋', '+'), ('，', ','), ('－', '-'), ('．', '.'), ('／', '/'),
    ('：', ':'), ('；', ';'), ('＜', '<'), ('＝', '='), ('＞', '>'),
    ('？', '?'), ('＠', '@'), ('［', '['), ('＼', '\\'), ('］', ']'),
    ('＾', '^'), ('＿', '_'), ('｀', '`'), ('｛', '{'), ('｜', '|'),
    ('｝', '}'), ('～', '~'),
    ('！\uFE00', '!'), ('！\uFE01', '!'), ('，\uFE00', ','), ('，\uFE01', ','),
    ('．\uFE00', '.'), ('．\uFE01', '.'), ('：\uFE00', ':'), ('：\uFE01', ':'),
    ('；\uFE00', ';'), ('；\uFE01', ';'), ('？\uFE00', '?'), ('？\uFE01', '?'),
    ('〜', '~'),
    ('　', '\u0020'),
])
def test_full_to_half(s, expect):
    cnv = FullToHalfConverter()
    actual = cnv.convert(s)
    if s == '〜':
        assert actual == s
    else:
        assert actual == expect

    config = ConverterConfig(punctuation=False)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    if s == '。' or s == '、' or s == '〜':
        assert actual == s
    else:
        assert actual == expect

    config = ConverterConfig(corner_brucket=False)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    if s == '「' or s == '」' or s == '〜':
        assert actual == s
    else:
        assert actual == expect

    config = ConverterConfig(conjunction_mark=False)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    if s == '・' or s == '〜':
        assert actual == s
    else:
        assert actual == expect

    config = ConverterConfig(length_mark=False)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    if s == 'ー' or s == '〜':
        assert actual == s
    else:
        assert actual == expect

    config = ConverterConfig(space=False)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    if s == '　' or s == '〜':
        assert actual == s
    else:
        assert actual == expect

    config = ConverterConfig(ascii_symbol=False)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    if s in [chr(c) for c in range(ord('！'), ord('／') + 1)] \
            or s in [chr(c) for c in range(ord('：'), ord('＠') + 1)] \
            or s in [chr(c) for c in range(ord('［'), ord('｀') + 1)] \
            or s in [chr(c) for c in range(ord('｛'), ord('～') + 1)] \
            or (len(s) >= 2 and s[0] in ['！', '，', '．', '：', '；', '？'] and s[1] in ['\uFE00', '\uFE01']) \
            or s == '〜':
        assert actual == s
    else:
        assert actual == expect

    config = ConverterConfig(ascii_digit=False)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    if s in [chr(c) for c in range(ord('０'), ord('９') + 1)] or s == '０\uFE00' or s == '\uFE00１\uFE00' \
            or s == '〜':
        assert actual == s
    else:
        assert actual == expect

    config = ConverterConfig(ascii_alphabet=False)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    if s in [chr(c) for c in range(ord('Ａ'), ord('Ｚ') + 1)] or s in [chr(c) for c in range(ord('ａ'), ord('ｚ') + 1)] \
            or s == '〜':
        assert actual == s
    else:
        assert actual == expect

    config = ConverterConfig(wave_dash=True)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)
    assert actual == expect


def test_full_to_half_with_controls():
    s = '\u30BF\u0000\u309B'
    cnv = FullToHalfConverter()
    actual = cnv.convert(s)
    assert actual == '\uFF80\u0000\u309B'


def test_full_to_half_invalid_parameter():
    cnv = FullToHalfConverter()

    with pytest.raises(TypeError, match='s must be a string.') as exc:
        cnv.convert(None)
