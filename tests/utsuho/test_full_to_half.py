import pytest

from utsuho.converters import FullToHalfConverter, WidthConverterConfig

test_data = [
    # カタカナ (清音)
    ('ア', 'ｱ'), ('イ', 'ｲ'), ('ウ', 'ｳ'), ('エ', 'ｴ'), ('オ', 'ｵ'),
    ('カ', 'ｶ'), ('キ', 'ｷ'), ('ク', 'ｸ'), ('ケ', 'ｹ'), ('コ', 'ｺ'),
    ('サ', 'ｻ'), ('シ', 'ｼ'), ('ス', 'ｽ'), ('セ', 'ｾ'), ('ソ', 'ｿ'),
    ('タ', 'ﾀ'), ('チ', 'ﾁ'), ('ツ', 'ﾂ'), ('テ', 'ﾃ'), ('ト', 'ﾄ'),
    ('ナ', 'ﾅ'), ('ニ', 'ﾆ'), ('ヌ', 'ﾇ'), ('ネ', 'ﾈ'), ('ノ', 'ﾉ'),
    ('ハ', 'ﾊ'), ('ヒ', 'ﾋ'), ('フ', 'ﾌ'), ('ヘ', 'ﾍ'), ('ホ', 'ﾎ'),
    ('マ', 'ﾏ'), ('ミ', 'ﾐ'), ('ム', 'ﾑ'), ('メ', 'ﾒ'), ('モ', 'ﾓ'),
    ('ヤ', 'ﾔ'), ('ユ', 'ﾕ'), ('ヨ', 'ﾖ'),
    ('ラ', 'ﾗ'), ('リ', 'ﾘ'), ('ル', 'ﾙ'), ('レ', 'ﾚ'), ('ロ', 'ﾛ'),
    ('ワ', 'ﾜ'), ('ヰ', 'ヰ'), ('ヱ', 'ヱ'),
    ('ヲ', 'ｦ'), ('ン', 'ﾝ'),
    # カタカナ (清音 [小書])
    ('ァ', 'ｧ'), ('ィ', 'ｨ'), ('ゥ', 'ｩ'), ('ェ', 'ｪ'), ('ォ', 'ｫ'),
    ('ッ', 'ｯ'), ('ャ', 'ｬ'), ('ュ', 'ｭ'), ('ョ', 'ｮ'),
    ('ヮ', 'ヮ'), ('ヵ', 'ヵ'), ('ヶ', 'ヶ'),
    # カタカナ (濁音)
    ('ガ', 'ｶ\uFF9E'), ('ギ', 'ｷ\uFF9E'), ('グ', 'ｸ\uFF9E'), ('ゲ', 'ｹ\uFF9E'), ('ゴ', 'ｺ\uFF9E'),
    ('ザ', 'ｻ\uFF9E'), ('ジ', 'ｼ\uFF9E'), ('ズ', 'ｽ\uFF9E'), ('ゼ', 'ｾ\uFF9E'), ('ゾ', 'ｿ\uFF9E'),
    ('ダ', 'ﾀ\uFF9E'), ('ヂ', 'ﾁ\uFF9E'), ('ヅ', 'ﾂ\uFF9E'), ('デ', 'ﾃ\uFF9E'), ('ド', 'ﾄ\uFF9E'),
    ('バ', 'ﾊ\uFF9E'), ('ビ', 'ﾋ\uFF9E'), ('ブ', 'ﾌ\uFF9E'), ('ベ', 'ﾍ\uFF9E'), ('ボ', 'ﾎ\uFF9E'),
    ('ヷ', 'ﾜ\uFF9E'), ('ヸ', 'ヸ'), ('ヴ', 'ｳ\uFF9E'), ('ヹ', 'ヹ'), ('ヺ', 'ｦ\uFF9E'),
    # カタカナ (半濁音)
    ('パ', 'ﾊ\uFF9F'), ('ピ', 'ﾋ\uFF9F'), ('プ', 'ﾌ\uFF9F'), ('ペ', 'ﾍ\uFF9F'), ('ポ', 'ﾎ\uFF9F'),
    # カタカナ (清音) + ひらがな (濁音記号)
    ('カ\u309B', 'ｶ\uFF9E'), ('キ\u309B', 'ｷ\uFF9E'), ('ク\u309B', 'ｸ\uFF9E'), ('ケ\u309B', 'ｹ\uFF9E'), ('コ\u309B', 'ｺ\uFF9E'),
    ('サ\u309B', 'ｻ\uFF9E'), ('シ\u309B', 'ｼ\uFF9E'), ('ス\u309B', 'ｽ\uFF9E'), ('セ\u309B', 'ｾ\uFF9E'), ('ソ\u309B', 'ｿ\uFF9E'),
    ('タ\u309B', 'ﾀ\uFF9E'), ('チ\u309B', 'ﾁ\uFF9E'), ('ツ\u309B', 'ﾂ\uFF9E'), ('テ\u309B', 'ﾃ\uFF9E'), ('ト\u309B', 'ﾄ\uFF9E'),
    ('ハ\u309B', 'ﾊ\uFF9E'), ('ヒ\u309B', 'ﾋ\uFF9E'), ('フ\u309B', 'ﾌ\uFF9E'), ('ヘ\u309B', 'ﾍ\uFF9E'), ('ホ\u309B', 'ﾎ\uFF9E'),
    ('ウ\u309B', 'ｳ\uFF9E'), ('ワ\u309B', 'ﾜ\uFF9E'), ('ヰ\u309B', 'ヰ\u309B'), ('ヱ\u309B', 'ヱ\u309B'), ('ヲ\u309B', 'ｦ\uFF9E'),
    # カタカナ (清音) + ひらがな (半濁音記号)
    ('ハ\u309C', 'ﾊ\uFF9F'), ('ヒ\u309C', 'ﾋ\uFF9F'), ('フ\u309C', 'ﾌ\uFF9F'), ('ヘ\u309C', 'ﾍ\uFF9F'), ('ホ\u309C', 'ﾎ\uFF9F'),
    # カタカナ (清音) + ひらがな (濁音記号 [結合文字])
    ('カ\u3099', 'ｶ\uFF9E'), ('キ\u3099', 'ｷ\uFF9E'), ('ク\u3099', 'ｸ\uFF9E'), ('ケ\u3099', 'ｹ\uFF9E'), ('コ\u3099', 'ｺ\uFF9E'),
    ('サ\u3099', 'ｻ\uFF9E'), ('シ\u3099', 'ｼ\uFF9E'), ('ス\u3099', 'ｽ\uFF9E'), ('セ\u3099', 'ｾ\uFF9E'), ('ソ\u3099', 'ｿ\uFF9E'),
    ('タ\u3099', 'ﾀ\uFF9E'), ('チ\u3099', 'ﾁ\uFF9E'), ('ツ\u3099', 'ﾂ\uFF9E'), ('テ\u3099', 'ﾃ\uFF9E'), ('ト\u3099', 'ﾄ\uFF9E'),
    ('ハ\u3099', 'ﾊ\uFF9E'), ('ヒ\u3099', 'ﾋ\uFF9E'), ('フ\u3099', 'ﾌ\uFF9E'), ('ヘ\u3099', 'ﾍ\uFF9E'), ('ホ\u3099', 'ﾎ\uFF9E'),
    ('ウ\u3099', 'ｳ\uFF9E'), ('ワ\u3099', 'ﾜ\uFF9E'), ('ヰ\u3099', 'ヰ\u3099'), ('ヱ\u3099', 'ヱ\u3099'), ('ヲ\u3099', 'ｦ\uFF9E'),
    # カタカナ (清音) + ひらがな (半濁音記号 [結合文字])
    ('ハ\u309A', 'ﾊ\uFF9F'), ('ヒ\u309A', 'ﾋ\uFF9F'), ('フ\u309A', 'ﾌ\uFF9F'), ('ヘ\u309A', 'ﾍ\uFF9F'), ('ホ\u309A', 'ﾎ\uFF9F'),
    # カタカナ (その他)
    ('゠', '゠'), ('・', '･'), ('ー', 'ｰ'), ('ヽ', 'ヽ'), ('ヾ', 'ヾ'),
    ('ヿ', 'ヿ'),
    # ひらがな (濁音・半濁音記号)
    ('\u309B', '\u309B'), ('\u309C', '\u309C'), ('\u3099', '\u3099'), ('\u309A', '\u309A'),
    # CJK 記号
    ('\u3000', '\u0020'), ('、', '､'), ('。', '｡'), ('「', '｢'), ('」', '｣'),
    # ASCII 記号
    ('！', '!'), ('＂', '"'), ('＃', '#'), ('＄', '$'), ('％', '%'),
    ('＆', '&'), ('＇', '\''), ('（', '('), ('）', ')'), ('＊', '*'),
    ('＋', '+'), ('，', ','), ('－', '-'), ('．', '.'), ('／', '/'),
    ('：', ':'), ('；', ';'), ('＜', '<'), ('＝', '='), ('＞', '>'),
    ('？', '?'), ('＠', '@'), ('［', '['), ('＼', '\\'), ('］', ']'),
    ('＾', '^'), ('＿', '_'), ('｀', '`'), ('｛', '{'), ('｜', '|'),
    ('｝', '}'), ('\uFF5E', '~'), ('\u301C', '~'), ('｟', '｟'), ('｠', '｠'),
    # ASCII 記号 + 異体字セレクター
    ('！\uFE00', '!'), ('！\uFE01', '!'), ('，\uFE00', ','), ('，\uFE01', ','),
    ('．\uFE00', '.'), ('．\uFE01', '.'), ('：\uFE00', ':'), ('：\uFE01', ':'),
    ('；\uFE00', ';'), ('；\uFE01', ';'), ('？\uFE00', '?'), ('？\uFE01', '?'),
    # ASCII 算用数字
    ('０', '0'), ('１', '1'), ('２', '2'), ('３', '3'), ('４', '4'),
    ('５', '5'), ('６', '6'), ('７', '7'), ('８', '8'), ('９', '9'),
    # ASCII 算用数字 + 異体字セレクター
    ('０\uFE00', '0\uFE00'),
    # ASCII アルファベット [大文字]
    ('Ａ', 'A'), ('Ｂ', 'B'), ('Ｃ', 'C'), ('Ｄ', 'D'), ('Ｅ', 'E'),
    ('Ｆ', 'F'), ('Ｇ', 'G'), ('Ｈ', 'H'), ('Ｉ', 'I'), ('Ｊ', 'J'),
    ('Ｋ', 'K'), ('Ｌ', 'L'), ('Ｍ', 'M'), ('Ｎ', 'N'), ('Ｏ', 'O'),
    ('Ｐ', 'P'), ('Ｑ', 'Q'), ('Ｒ', 'R'), ('Ｓ', 'S'), ('Ｔ', 'T'),
    ('Ｕ', 'U'), ('Ｖ', 'V'), ('Ｗ', 'W'), ('Ｘ', 'X'), ('Ｙ', 'Y'),
    ('Ｚ', 'Z'),
    # ASCII アルファベット [小文字]
    ('ａ', 'a'), ('ｂ', 'b'), ('ｃ', 'c'), ('ｄ', 'd'), ('ｅ', 'e'),
    ('ｆ', 'f'), ('ｇ', 'g'), ('ｈ', 'h'), ('ｉ', 'i'), ('ｊ', 'j'),
    ('ｋ', 'k'), ('ｌ', 'l'), ('ｍ', 'm'), ('ｎ', 'n'), ('ｏ', 'o'),
    ('ｐ', 'p'), ('ｑ', 'q'), ('ｒ', 'r'), ('ｓ', 's'), ('ｔ', 't'),
    ('ｕ', 'u'), ('ｖ', 'v'), ('ｗ', 'w'), ('ｘ', 'x'), ('ｙ', 'y'),
    ('ｚ', 'z'),
    # 異体字セレクター
    ('\uFE00', '\uFE00'), ('\uFE01', '\uFE01'), ('\uFE02', '\uFE02'), ('\uFE03', '\uFE03'), ('\uFE04', '\uFE04'),
    ('\uFE05', '\uFE05'), ('\uFE06', '\uFE06'), ('\uFE07', '\uFE07'), ('\uFE08', '\uFE08'), ('\uFE09', '\uFE09'),
    ('\uFE0A', '\uFE0A'), ('\uFE0B', '\uFE0B'), ('\uFE0C', '\uFE0C'), ('\uFE0D', '\uFE0D'), ('\uFE0E', '\uFE0E'),
    ('\uFE0F', '\uFE0F'),
    # 濁音・半濁音記号 [カタカナに続く]
    ('ガ\u309B', 'ｶ\uFF9E\uFF9E'), ('ガ\u3099', 'ｶ\uFF9E\uFF9E'),
    ('カ\u309B\u309B', 'ｶ\uFF9E\uFF9E'), ('カ\u3099\u3099', 'ｶ\uFF9E\uFF9E'),
    ('カ\u3099\u309B', 'ｶ\uFF9E\uFF9E'), ('カ\u309B\u3099', 'ｶ\uFF9E\uFF9E'),
    ('パ\u309C', 'ﾊ\uFF9F\uFF9F'), ('パ\u309A', 'ﾊ\uFF9F\uFF9F'),
    ('ハ\u309C\u309C', 'ﾊ\uFF9F\uFF9F'), ('ハ\u309A\u309A', 'ﾊ\uFF9F\uFF9F'),
    ('ハ\u309A\u309C', 'ﾊ\uFF9F\uFF9F'), ('ハ\u309C\u309A', 'ﾊ\uFF9F\uFF9F'),
    # 濁音・半濁音記号 [カタカナに続かない]
    ('が\u309B', 'が\u309B'), ('が\u3099', 'が\u3099'),
    ('か\u309B\u309B', 'か\u309B\u309B'), ('か\u3099\u3099', 'か\u3099\u3099'),
    ('か\u3099\u309B', 'か\u3099\u309B'), ('か\u309B\u3099', 'か\u309B\u3099'),
    ('ぱ\u309C', 'ぱ\u309C'), ('ぱ\u309A', 'ぱ\u309A'),
    ('は\u309C\u309C', 'は\u309C\u309C'), ('は\u309A\u309A', 'は\u309A\u309A'),
    ('は\u309A\u309C', 'は\u309A\u309C'), ('は\u309C\u309A', 'は\u309C\u309A'),
    ('ｶ\uFF9E\u309B', 'ｶ\uFF9E\u309B'), ('ｶ\uFF9E\u3099', 'ｶ\uFF9E\u3099'),
    ('ﾊ\uFF9F\u309C', 'ﾊ\uFF9F\u309C'), ('ﾊ\uFF9F\u309A', 'ﾊ\uFF9F\u309A'),
    ('カ\u0000\u309B', 'ｶ\u0000\u309B'), ('カ\u0000\u3099', 'ｶ\u0000\u3099'),
    ('ハ\u0000\u309C', 'ﾊ\u0000\u309C'), ('ハ\u0000\u309A', 'ﾊ\u0000\u309A'),
    # 無効な異体字セレクター [変換対象に続く]
    ('ア\uFE00', 'ｱ'),
    # 無効な異体字セレクター [変換対象に続かない]
    ('亜\uFE00', '亜\uFE00'),
]


@pytest.mark.parametrize('s,expect', test_data)
def test_full_to_half(s, expect):
    cnv = FullToHalfConverter()
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in ['\u301C',]) else s
    )


@pytest.mark.parametrize('s,expect', test_data)
def test_full_to_half_without_punctuations(s, expect):
    config = WidthConverterConfig(punctuation=False, wave_dash=True)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in ['、', '。',]) else s
    )


@pytest.mark.parametrize('s,expect', test_data)
def test_full_to_half_without_corner_bruckets(s, expect):
    config = WidthConverterConfig(corner_brucket=False, wave_dash=True)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in ['「', '」',]) else s
    )


@pytest.mark.parametrize('s,expect', test_data)
def test_full_to_half_without_conjunction_marks(s, expect):
    config = WidthConverterConfig(conjunction_mark=False, wave_dash=True)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in ['・',]) else s
    )


@pytest.mark.parametrize('s,expect', test_data)
def test_full_to_half_without_length_marks(s, expect):
    config = WidthConverterConfig(length_mark=False, wave_dash=True)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in ['ー',]) else s
    )


@pytest.mark.parametrize('s,expect', test_data)
def test_full_to_half_without_spaces(s, expect):
    config = WidthConverterConfig(space=False, wave_dash=True)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in ['\u3000',]) else s
    )


@pytest.mark.parametrize('s,expect', test_data)
def test_full_to_half_without_ascii_symbols(s, expect):
    config = WidthConverterConfig(ascii_symbol=False, wave_dash=True)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in [
            '！', '＂', '＃', '＄', '％', '＆', '＇', '（', '）', '＊', '＋', '，', '－', '．', '／', '：',
            '；', '＜', '＝', '＞', '？', '＠', '［', '＼', '］', '＾', '＿', '｀', '｛', '｜', '｝', '\uFF5E',
            '！\uFE00', '，\uFE00', '．\uFE00', '：\uFE00', '；\uFE00', '？\uFE00',
            '！\uFE01', '，\uFE01', '．\uFE01', '：\uFE01', '；\uFE01', '？\uFE01',
        ]) else s
    )


@pytest.mark.parametrize('s,expect', test_data)
def test_full_to_half_without_ascii_digits(s, expect):
    config = WidthConverterConfig(ascii_digit=False, wave_dash=True)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in [
            "０", "１", "２", "３", "４", "５", "６", "７", "８", "９",
            "０\uFE00",
        ]) else s
    )


@pytest.mark.parametrize('s,expect', test_data)
def test_full_to_half_without_ascii_alphabets(s, expect):
    config = WidthConverterConfig(ascii_alphabet=False, wave_dash=True)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in [
            'Ａ', 'Ｂ', 'Ｃ', 'Ｄ', 'Ｅ', 'Ｆ', 'Ｇ', 'Ｈ', 'Ｉ', 'Ｊ', 'Ｋ', 'Ｌ', 'Ｍ',
            'Ｎ', 'Ｏ', 'Ｐ', 'Ｑ', 'Ｒ', 'Ｓ', 'Ｔ', 'Ｕ', 'Ｖ', 'Ｗ', 'Ｘ', 'Ｙ', 'Ｚ',
            'ａ', 'ｂ', 'ｃ', 'ｄ', 'ｅ', 'ｆ', 'ｇ', 'ｈ', 'ｉ', 'ｊ', 'ｋ', 'ｌ', 'ｍ',
            'ｎ', 'ｏ', 'ｐ', 'ｑ', 'ｒ', 'ｓ', 'ｔ', 'ｕ', 'ｖ', 'ｗ', 'ｘ', 'ｙ', 'ｚ',
        ]) else s
    )


@pytest.mark.parametrize('s,expect', test_data)
def test_full_to_half_without_wave_dash(s, expect):
    config = WidthConverterConfig(wave_dash=False)
    cnv = FullToHalfConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect if not (s in [
            '\u301C',
        ]) else s
    )


def test_full_to_half_with_invalid_parameter():
    cnv = FullToHalfConverter()

    with pytest.raises(TypeError, match='s must be a string.') as exc:
        cnv.convert(None)
