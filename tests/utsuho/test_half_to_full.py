import pytest

from utsuho.converters import HalfToFullConverter, WidthConverterConfig

test_data = [
    # カタカナ (清音)
    ("ｱ", "ア"),
    ("ｲ", "イ"),
    ("ｳ", "ウ"),
    ("ｴ", "エ"),
    ("ｵ", "オ"),
    ("ｶ", "カ"),
    ("ｷ", "キ"),
    ("ｸ", "ク"),
    ("ｹ", "ケ"),
    ("ｺ", "コ"),
    ("ｻ", "サ"),
    ("ｼ", "シ"),
    ("ｽ", "ス"),
    ("ｾ", "セ"),
    ("ｿ", "ソ"),
    ("ﾀ", "タ"),
    ("ﾁ", "チ"),
    ("ﾂ", "ツ"),
    ("ﾃ", "テ"),
    ("ﾄ", "ト"),
    ("ﾅ", "ナ"),
    ("ﾆ", "ニ"),
    ("ﾇ", "ヌ"),
    ("ﾈ", "ネ"),
    ("ﾉ", "ノ"),
    ("ﾊ", "ハ"),
    ("ﾋ", "ヒ"),
    ("ﾌ", "フ"),
    ("ﾍ", "ヘ"),
    ("ﾎ", "ホ"),
    ("ﾏ", "マ"),
    ("ﾐ", "ミ"),
    ("ﾑ", "ム"),
    ("ﾒ", "メ"),
    ("ﾓ", "モ"),
    ("ﾔ", "ヤ"),
    ("ﾕ", "ユ"),
    ("ﾖ", "ヨ"),
    ("ﾗ", "ラ"),
    ("ﾘ", "リ"),
    ("ﾙ", "ル"),
    ("ﾚ", "レ"),
    ("ﾛ", "ロ"),
    ("ﾜ", "ワ"),
    ("ｦ", "ヲ"),
    ("ﾝ", "ン"),
    # カタカナ (清音 [小書])
    ("ｧ", "ァ"),
    ("ｨ", "ィ"),
    ("ｩ", "ゥ"),
    ("ｪ", "ェ"),
    ("ｫ", "ォ"),
    ("ｯ", "ッ"),
    ("ｬ", "ャ"),
    ("ｭ", "ュ"),
    ("ｮ", "ョ"),
    # カタカナ (濁音)
    ("ｶ\uff9e", "ガ"),
    ("ｷ\uff9e", "ギ"),
    ("ｸ\uff9e", "グ"),
    ("ｹ\uff9e", "ゲ"),
    ("ｺ\uff9e", "ゴ"),
    ("ｻ\uff9e", "ザ"),
    ("ｼ\uff9e", "ジ"),
    ("ｽ\uff9e", "ズ"),
    ("ｾ\uff9e", "ゼ"),
    ("ｿ\uff9e", "ゾ"),
    ("ﾀ\uff9e", "ダ"),
    ("ﾁ\uff9e", "ヂ"),
    ("ﾂ\uff9e", "ヅ"),
    ("ﾃ\uff9e", "デ"),
    ("ﾄ\uff9e", "ド"),
    ("ﾊ\uff9e", "バ"),
    ("ﾋ\uff9e", "ビ"),
    ("ﾌ\uff9e", "ブ"),
    ("ﾍ\uff9e", "ベ"),
    ("ﾎ\uff9e", "ボ"),
    ("ﾜ\uff9e", "ヷ"),
    ("ｳ\uff9e", "ヴ"),
    ("ｦ\uff9e", "ヺ"),
    # カタカナ (半濁音)
    ("ﾊ\uff9f", "パ"),
    ("ﾋ\uff9f", "ピ"),
    ("ﾌ\uff9f", "プ"),
    ("ﾍ\uff9f", "ペ"),
    ("ﾎ\uff9f", "ポ"),
    # カタカナ (その他)
    ("･", "・"),
    ("ｰ", "ー"),
    # ひらがな (濁音・半濁音記号)
    ("\uff9e", "\u309b"),
    ("\uff9f", "\u309c"),
    # CJK 記号
    ("､", "、"),
    ("｡", "。"),
    ("｢", "「"),
    ("｣", "」"),
    # スペース
    ("\u0020", "\u3000"),
    ("\u00a0", "\u3000"),
    # ASCII 記号
    ("!", "！"),
    ("\"", "＂"),
    ("#", "＃"),
    ("$", "＄"),
    ("%", "％"),
    ("&", "＆"),
    ("'", "＇"),
    ("(", "（"),
    (")", "）"),
    ("*", "＊"),
    ("+", "＋"),
    (",", "，"),
    ("-", "－"),
    (".", "．"),
    ("/", "／"),
    (":", "："),
    (";", "；"),
    ("<", "＜"),
    ("=", "＝"),
    (">", "＞"),
    ("?", "？"),
    ("@", "＠"),
    ("[", "［"),
    ("\\", "＼"),
    ("]", "］"),
    ("^", "＾"),
    ("_", "＿"),
    ("`", "｀"),
    ("{", "｛"),
    ("|", "｜"),
    ("}", "｝"),
    ("~", "\uff5e"),
    # ASCII 算用数字
    ("0", "０"),
    ("1", "１"),
    ("2", "２"),
    ("3", "３"),
    ("4", "４"),
    ("5", "５"),
    ("6", "６"),
    ("7", "７"),
    ("8", "８"),
    ("9", "９"),
    # ASCII 算用数字 + 異体字セレクター
    ("0\ufe00", "０\ufe00"),
    # ASCII アルファベット [大文字]
    ("A", "Ａ"),
    ("B", "Ｂ"),
    ("C", "Ｃ"),
    ("D", "Ｄ"),
    ("E", "Ｅ"),
    ("F", "Ｆ"),
    ("G", "Ｇ"),
    ("H", "Ｈ"),
    ("I", "Ｉ"),
    ("J", "Ｊ"),
    ("K", "Ｋ"),
    ("L", "Ｌ"),
    ("M", "Ｍ"),
    ("N", "Ｎ"),
    ("O", "Ｏ"),
    ("P", "Ｐ"),
    ("Q", "Ｑ"),
    ("R", "Ｒ"),
    ("S", "Ｓ"),
    ("T", "Ｔ"),
    ("U", "Ｕ"),
    ("V", "Ｖ"),
    ("W", "Ｗ"),
    ("X", "Ｘ"),
    ("Y", "Ｙ"),
    ("Z", "Ｚ"),
    # ASCII アルファベット [小文字]
    ("a", "ａ"),
    ("b", "ｂ"),
    ("c", "ｃ"),
    ("d", "ｄ"),
    ("e", "ｅ"),
    ("f", "ｆ"),
    ("g", "ｇ"),
    ("h", "ｈ"),
    ("i", "ｉ"),
    ("j", "ｊ"),
    ("k", "ｋ"),
    ("l", "ｌ"),
    ("m", "ｍ"),
    ("n", "ｎ"),
    ("o", "ｏ"),
    ("p", "ｐ"),
    ("q", "ｑ"),
    ("r", "ｒ"),
    ("s", "ｓ"),
    ("t", "ｔ"),
    ("u", "ｕ"),
    ("v", "ｖ"),
    ("w", "ｗ"),
    ("x", "ｘ"),
    ("y", "ｙ"),
    ("z", "ｚ"),
    # 濁音・半濁音記号 [全角で合成済み文字が定義されていない]
    ("ｱ\uff9e", "ア\u309b"),
    ("ｶ\uff9e\uff9e", "ガ\u309b"),
    ("ｱ\uff9f", "ア\u309c"),
    ("ﾊ\uff9f\uff9f", "パ\u309c"),
    # 異体字セレクター
    ("\ufe00", "\ufe00"),
    ("\ufe01", "\ufe01"),
    ("\ufe02", "\ufe02"),
    ("\ufe03", "\ufe03"),
    ("\ufe04", "\ufe04"),
    ("\ufe05", "\ufe05"),
    ("\ufe06", "\ufe06"),
    ("\ufe07", "\ufe07"),
    ("\ufe08", "\ufe08"),
    ("\ufe09", "\ufe09"),
    ("\ufe0a", "\ufe0a"),
    ("\ufe0b", "\ufe0b"),
    ("\ufe0c", "\ufe0c"),
    ("\ufe0d", "\ufe0d"),
    ("\ufe0e", "\ufe0e"),
    ("\ufe0f", "\ufe0f"),
    # 無効な異体字セレクター [変換対象に続く]
    # ("ｱ\uFE00", "ア"),
    # 無効な異体字セレクター [変換対象に続かない]
    ("亜\ufe00", "亜\ufe00"),
]


@pytest.mark.parametrize("s,expect", test_data)
def test_half_to_full(
    s,
    expect,
):
    cnv = HalfToFullConverter()
    actual = cnv.convert(s)

    assert actual == expect


@pytest.mark.parametrize("s,expect", test_data)
def test_half_to_full_without_punctuations(
    s,
    expect,
):
    config = WidthConverterConfig(punctuation=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == (expect if not (s in ["､", "｡"]) else s)


@pytest.mark.parametrize("s,expect", test_data)
def test_half_to_full_without_corner_bruckets(
    s,
    expect,
):
    config = WidthConverterConfig(corner_brucket=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect
        if not (
            s
            in [
                "｢",
                "｣",
            ]
        )
        else s
    )


@pytest.mark.parametrize("s,expect", test_data)
def test_half_to_full_without_conjunction_marks(
    s,
    expect,
):
    config = WidthConverterConfig(conjunction_mark=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect
        if not (
            s
            in [
                "･",
            ]
        )
        else s
    )


@pytest.mark.parametrize("s,expect", test_data)
def test_half_to_full_without_length_marks(
    s,
    expect,
):
    config = WidthConverterConfig(length_mark=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect
        if not (
            s
            in [
                "ｰ",
            ]
        )
        else s
    )


@pytest.mark.parametrize("s,expect", test_data)
def test_half_to_full_without_spaces(
    s,
    expect,
):
    config = WidthConverterConfig(space=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect
        if not (
            s
            in [
                "\u0020",
                "\u00a0",
            ]
        )
        else s
    )


@pytest.mark.parametrize("s,expect", test_data)
def test_half_to_full_without_ascii_symbols(
    s,
    expect,
):
    config = WidthConverterConfig(ascii_symbol=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect
        if not (
            s
            in [
                "!",
                "\"",
                "#",
                "$",
                "%",
                "&",
                "'",
                "(",
                ")",
                "*",
                "+",
                ",",
                "-",
                ".",
                "/",
                ":",
                ";",
                "<",
                "=",
                ">",
                "?",
                "@",
                "[",
                "\\",
                "]",
                "^",
                "_",
                "`",
                "{",
                "|",
                "}",
                "~",
            ]
        )
        else s
    )


@pytest.mark.parametrize("s,expect", test_data)
def test_half_to_full_without_ascii_digits(
    s,
    expect,
):
    config = WidthConverterConfig(ascii_digit=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect
        if not (
            s
            in [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "0\ufe00",
            ]
        )
        else s
    )


@pytest.mark.parametrize("s,expect", test_data)
def test_half_to_full_without_ascii_alphabets(
    s,
    expect,
):
    config = WidthConverterConfig(ascii_alphabet=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == (
        expect
        if not (
            s
            in [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "I",
                "J",
                "K",
                "L",
                "M",
                "N",
                "O",
                "P",
                "Q",
                "R",
                "S",
                "T",
                "U",
                "V",
                "W",
                "X",
                "Y",
                "Z",
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
                "g",
                "h",
                "i",
                "j",
                "k",
                "l",
                "m",
                "n",
                "o",
                "p",
                "q",
                "r",
                "s",
                "t",
                "u",
                "v",
                "w",
                "x",
                "y",
                "z",
            ]
        )
        else s
    )


@pytest.mark.parametrize("s,expect", test_data)
def test_half_to_full_without_wave_dash(
    s,
    expect,
):
    config = WidthConverterConfig(wave_dash=False)
    cnv = HalfToFullConverter(config)
    actual = cnv.convert(s)

    assert actual == expect


def test_half_to_full_with_invalid_parameter():
    cnv = HalfToFullConverter()

    with pytest.raises(TypeError, match="s must be a string."):
        cnv.convert(None)  # type: ignore
