import pytest

from utsuho.converters import WidthConverterConfig, HalfToFullConverter

test_data = [
    # カタカナ (清音)
    ('ｱ', 'ア'), ('ｲ', 'イ'), ('ｳ', 'ウ'), ('ｴ', 'エ'), ('ｵ', 'オ'),
    ('ｶ', 'カ'), ('ｷ', 'キ'), ('ｸ', 'ク'), ('ｹ', 'ケ'), ('ｺ', 'コ'),
    ('ｻ', 'サ'), ('ｼ', 'シ'), ('ｽ', 'ス'), ('ｾ', 'セ'), ('ｿ', 'ソ'),
    ('ﾀ', 'タ'), ('ﾁ', 'チ'), ('ﾂ', 'ツ'), ('ﾃ', 'テ'), ('ﾄ', 'ト'),
    ('ﾅ', 'ナ'), ('ﾆ', 'ニ'), ('ﾇ', 'ヌ'), ('ﾈ', 'ネ'), ('ﾉ', 'ノ'),
    ('ﾊ', 'ハ'), ('ﾋ', 'ヒ'), ('ﾌ', 'フ'), ('ﾍ', 'ヘ'), ('ﾎ', 'ホ'),
    ('ﾏ', 'マ'), ('ﾐ', 'ミ'), ('ﾑ', 'ム'), ('ﾒ', 'メ'), ('ﾓ', 'モ'),
    ('ﾔ', 'ヤ'), ('ﾕ', 'ユ'), ('ﾖ', 'ヨ'),
    ('ﾗ', 'ラ'), ('ﾘ', 'リ'), ('ﾙ', 'ル'), ('ﾚ', 'レ'), ('ﾛ', 'ロ'),
    ('ﾜ', 'ワ'),
    ('ｦ', 'ヲ'), ('ﾝ', 'ン'),
    # カタカナ (清音 [小書])
    ('ｧ', 'ァ'), ('ｨ', 'ィ'), ('ｩ', 'ゥ'), ('ｪ', 'ェ'), ('ｫ', 'ォ'),
    ('ｯ', 'ッ'), ('ｬ', 'ャ'), ('ｭ', 'ュ'), ('ｮ', 'ョ'),
    # カタカナ (濁音)
    ('ｶ\uFF9E', 'ガ'), ('ｷ\uFF9E', 'ギ'), ('ｸ\uFF9E', 'グ'), ('ｹ\uFF9E', 'ゲ'), ('ｺ\uFF9E', 'ゴ'),
    ('ｻ\uFF9E', 'ザ'), ('ｼ\uFF9E', 'ジ'), ('ｽ\uFF9E', 'ズ'), ('ｾ\uFF9E', 'ゼ'), ('ｿ\uFF9E', 'ゾ'),
    ('ﾀ\uFF9E', 'ダ'), ('ﾁ\uFF9E', 'ヂ'), ('ﾂ\uFF9E', 'ヅ'), ('ﾃ\uFF9E', 'デ'), ('ﾄ\uFF9E', 'ド'),
    ('ﾊ\uFF9E', 'バ'), ('ﾋ\uFF9E', 'ビ'), ('ﾌ\uFF9E', 'ブ'), ('ﾍ\uFF9E', 'ベ'), ('ﾎ\uFF9E', 'ボ'),
    ('ﾜ\uFF9E', 'ヷ'), ('ｳ\uFF9E', 'ヴ'), ('ｦ\uFF9E', 'ヺ'),
    # カタカナ (半濁音)
    ('ﾊ\uFF9F', 'パ'), ('ﾋ\uFF9F', 'ピ'), ('ﾌ\uFF9F', 'プ'), ('ﾍ\uFF9F', 'ペ'), ('ﾎ\uFF9F', 'ポ'),
    # カタカナ (その他)
    ('･', '・'), ('ｰ', 'ー'),
    # ひらがな (濁音・半濁音記号)
    ('\uFF9E', '\u309B'), ('\uFF9F', '\u309C'),
    # CJK 記号
    ('､', '、'), ('｡', '。'), ('｢', '「'), ('｣', '」'),
    # スペース
    ('\u0020', '\u3000'), ('\u00A0', '\u3000'),
    # ASCII 記号
    ('!', '！'), ('"', '＂'), ('#', '＃'), ('$', '＄'), ('%', '％'),
    ('&', '＆'), ('\'', '＇'), ('(', '（'), (')', '）'), ('*', '＊'),
    ('+', '＋'), (',', '，'), ('-', '－'), ('.', '．'), ('/', '／'),
    (':', '：'), (';', '；'), ('<', '＜'), ('=', '＝'), ('>', '＞'),
    ('?', '？'), ('@', '＠'), ('[', '［'), ('\\', '＼'), (']', '］'),
    ('^', '＾'), ('_', '＿'), ('`', '｀'), ('{', '｛'), ('|', '｜'),
    ('}', '｝'), ('~', '\uFF5E'),
    # ASCII 算用数字
    ('0', '０'), ('1', '１'), ('2', '２'), ('3', '３'), ('4', '４'),
    ('5', '５'), ('6', '６'), ('7', '７'), ('8', '８'), ('9', '９'),
    # ASCII 算用数字 + 異体字セレクター
    ('0\uFE00', '０\uFE00'),
    # ASCII アルファベット [大文字]
    ('A', 'Ａ'), ('B', 'Ｂ'), ('C', 'Ｃ'), ('D', 'Ｄ'), ('E', 'Ｅ'),
    ('F', 'Ｆ'), ('G', 'Ｇ'), ('H', 'Ｈ'), ('I', 'Ｉ'), ('J', 'Ｊ'),
    ('K', 'Ｋ'), ('L', 'Ｌ'), ('M', 'Ｍ'), ('N', 'Ｎ'), ('O', 'Ｏ'),
    ('P', 'Ｐ'), ('Q', 'Ｑ'), ('R', 'Ｒ'), ('S', 'Ｓ'), ('T', 'Ｔ'),
    ('U', 'Ｕ'), ('V', 'Ｖ'), ('W', 'Ｗ'), ('X', 'Ｘ'), ('Y', 'Ｙ'),
    ('Z', 'Ｚ'),
    # ASCII アルファベット [小文字]
    ('a', 'ａ'), ('b', 'ｂ'), ('c', 'ｃ'), ('d', 'ｄ'), ('e', 'ｅ'),
    ('f', 'ｆ'), ('g', 'ｇ'), ('h', 'ｈ'), ('i', 'ｉ'), ('j', 'ｊ'),
    ('k', 'ｋ'), ('l', 'ｌ'), ('m', 'ｍ'), ('n', 'ｎ'), ('o', 'ｏ'),
    ('p', 'ｐ'), ('q', 'ｑ'), ('r', 'ｒ'), ('s', 'ｓ'), ('t', 'ｔ'),
    ('u', 'ｕ'), ('v', 'ｖ'), ('w', 'ｗ'), ('x', 'ｘ'), ('y', 'ｙ'),
    ('z', 'ｚ'),
    # 濁音・半濁音記号 [全角で合成済み文字が定義されていない]
    ('ｱ\uFF9E', 'ア\u309B'), ('ｶ\uFF9E\uFF9E', 'ガ\u309B'),
    ('ｱ\uFF9F', 'ア\u309C'), ('ﾊ\uFF9F\uFF9F', 'パ\u309C'),
    # 異体字セレクター
    ('\uFE00', '\uFE00'), ('\uFE01', '\uFE01'), ('\uFE02', '\uFE02'), ('\uFE03', '\uFE03'), ('\uFE04', '\uFE04'),
    ('\uFE05', '\uFE05'), ('\uFE06', '\uFE06'), ('\uFE07', '\uFE07'), ('\uFE08', '\uFE08'), ('\uFE09', '\uFE09'),
    ('\uFE0A', '\uFE0A'), ('\uFE0B', '\uFE0B'), ('\uFE0C', '\uFE0C'), ('\uFE0D', '\uFE0D'), ('\uFE0E', '\uFE0E'),
    ('\uFE0F', '\uFE0F'),
    # 無効な異体字セレクター [変換対象に続く]
    # ('ｱ\uFE00', 'ア'),
    # 無効な異体字セレクター [変換対象に続かない]
    ('亜\uFE00', '亜\uFE00'),
]


@pytest.mark.parametrize('s,expect', test_data)
def test_half_to_full(s, expect):
    cnv = HalfToFullConverter()
    actual = cnv.convert(s)

    assert actual == expect


@pytest.mark.parametrize('s,expect', test_data)
def test_half_to_full_without_punctuations(s, expect):
    config = WidthConverterConfig(punctuation=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in ['､', '｡']) else s
    )


@pytest.mark.parametrize('s,expect', test_data)
def test_half_to_full_without_corner_bruckets(s, expect):
    config = WidthConverterConfig(corner_brucket=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in ['｢', '｣',]) else s
    )


@pytest.mark.parametrize('s,expect', test_data)
def test_half_to_full_without_conjunction_marks(s, expect):
    config = WidthConverterConfig(conjunction_mark=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in ['･',]) else s
    )


@pytest.mark.parametrize('s,expect', test_data)
def test_half_to_full_without_length_marks(s, expect):
    config = WidthConverterConfig(length_mark=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in ['ｰ',]) else s
    )


@pytest.mark.parametrize('s,expect', test_data)
def test_half_to_full_without_spaces(s, expect):
    config = WidthConverterConfig(space=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in ['\u0020', '\u00A0',]) else s
    )


@pytest.mark.parametrize('s,expect', test_data)
def test_half_to_full_without_ascii_symbols(s, expect):
    config = WidthConverterConfig(ascii_symbol=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in [
            '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':',
            ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
        ]) else s
    )


@pytest.mark.parametrize('s,expect', test_data)
def test_half_to_full_without_ascii_digits(s, expect):
    config = WidthConverterConfig(ascii_digit=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in [
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
            "0\uFE00",
        ]) else s
    )


@pytest.mark.parametrize('s,expect', test_data)
def test_half_to_full_without_ascii_alphabets(s, expect):
    config = WidthConverterConfig(ascii_alphabet=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        ]) else s
    )


@pytest.mark.parametrize('s,expect', test_data)
def test_half_to_full_without_wave_dash(s, expect):
    config = WidthConverterConfig(wave_dash=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == expect


def test_half_to_full_with_invalid_parameter():
    cnv = HalfToFullConverter()

    with pytest.raises(TypeError, match='s must be a string.') as exc:
        cnv.convert(None)
