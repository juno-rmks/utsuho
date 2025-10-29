from utsuho.converters import (
    FullToHalfConverter,
    HalfToFullConverter,
    HiraganaToKatakanaConverter,
    KatakanaToHiraganaConverter,
)


def test_half_to_full_mix(benchmark):
    # seion=50%, dakuon=20%, handakuon=10%, fullwidth=20%
    s = ("ﾊ" * 50) + ("ﾊﾞ" * 20) + ("ﾊﾟ" * 10) + ("ハ" * 20)
    cnv = HalfToFullConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == ("ハ" * 50) + ("バ" * 20) + ("パ" * 10) + ("ハ" * 20)


def test_half_to_full_seion(benchmark):
    s = "ﾊ" * 100
    cnv = HalfToFullConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == "ハ" * 100


def test_half_to_full_dakuon(benchmark):
    s = "ﾊﾞ" * 100
    cnv = HalfToFullConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == "バ" * 100


def test_half_to_full_handakuon(benchmark):
    s = "ﾊﾟ" * 100
    cnv = HalfToFullConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == "パ" * 100


def test_half_to_full_fullwidth(benchmark):
    s = "ハ" * 100
    cnv = HalfToFullConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == "ハ" * 100


def test_full_to_half_mix(benchmark):
    # seion=50%, dakuon=20%, handakuon=10%, halfwidth=20%
    s = ("ハ" * 50) + ("バ" * 20) + ("パ" * 10) + ("ﾊ" * 20)
    cnv = FullToHalfConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == ("ﾊ" * 50) + ("ﾊﾞ" * 20) + ("ﾊﾟ" * 10) + ("ﾊ" * 20)


def test_full_to_half_seion(benchmark):
    s = "ハ" * 100
    cnv = FullToHalfConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == "ﾊ" * 100


def test_full_to_half_dakuon(benchmark):
    s = "バ" * 100
    cnv = FullToHalfConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == "ﾊﾞ" * 100


def test_full_to_half_handakuon(benchmark):
    s = "パ" * 100
    cnv = FullToHalfConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == "ﾊﾟ" * 100


def test_full_to_half_halfwidth(benchmark):
    s = "ﾊ" * 100
    cnv = FullToHalfConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == "ﾊ" * 100


def test_hiragana_to_katakana(benchmark):
    s = "あ" * 100
    cnv = HiraganaToKatakanaConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == "ア" * 100


def test_katakana_to_hiragana(benchmark):
    s = "ア" * 100
    cnv = KatakanaToHiraganaConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == "あ" * 100
