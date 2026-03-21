"""
Performance benchmarks for the Utsuho converters.
"""

from utsuho.converters import (
    FullToHalfConverter,
    HalfToFullConverter,
    HiraganaToKatakanaConverter,
    KatakanaToHiraganaConverter,
)

BENCHMARK_REPEAT = 1000


def test_half_to_full_mix(benchmark):
    """
    Benchmark half-width to full-width conversion with mixed-width input.
    """
    # seion=50%, dakuon=20%, handakuon=10%, fullwidth=20%
    s = (("ﾊ" * 50) + ("ﾊﾞ" * 20) + ("ﾊﾟ" * 10) + ("ハ" * 20)) * BENCHMARK_REPEAT
    cnv = HalfToFullConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == (
        (("ハ" * 50) + ("バ" * 20) + ("パ" * 10) + ("ハ" * 20)) * BENCHMARK_REPEAT
    )


def test_half_to_full_seion(benchmark):
    """
    Benchmark half-width to full-width conversion for unvoiced kana input.
    """
    s = ("ﾊ" * 100) * BENCHMARK_REPEAT
    cnv = HalfToFullConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == ("ハ" * 100) * BENCHMARK_REPEAT


def test_half_to_full_dakuon(benchmark):
    """
    Benchmark half-width to full-width conversion for voiced kana input.
    """
    s = ("ﾊﾞ" * 100) * BENCHMARK_REPEAT
    cnv = HalfToFullConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == ("バ" * 100) * BENCHMARK_REPEAT


def test_half_to_full_handakuon(benchmark):
    """
    Benchmark half-width to full-width conversion for semi-voiced kana input.
    """
    s = ("ﾊﾟ" * 100) * BENCHMARK_REPEAT
    cnv = HalfToFullConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == ("パ" * 100) * BENCHMARK_REPEAT


def test_half_to_full_fullwidth(benchmark):
    """
    Benchmark half-width to full-width conversion for already full-width input.
    """
    s = ("ハ" * 100) * BENCHMARK_REPEAT
    cnv = HalfToFullConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == ("ハ" * 100) * BENCHMARK_REPEAT


def test_full_to_half_mix(benchmark):
    """
    Benchmark full-width to half-width conversion with mixed-width input.
    """
    # seion=50%, dakuon=20%, handakuon=10%, halfwidth=20%
    s = (("ハ" * 50) + ("バ" * 20) + ("パ" * 10) + ("ﾊ" * 20)) * BENCHMARK_REPEAT
    cnv = FullToHalfConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == (
        (("ﾊ" * 50) + ("ﾊﾞ" * 20) + ("ﾊﾟ" * 10) + ("ﾊ" * 20)) * BENCHMARK_REPEAT
    )


def test_full_to_half_seion(benchmark):
    """
    Benchmark full-width to half-width conversion for unvoiced kana input.
    """
    s = ("ハ" * 100) * BENCHMARK_REPEAT
    cnv = FullToHalfConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == ("ﾊ" * 100) * BENCHMARK_REPEAT


def test_full_to_half_dakuon(benchmark):
    """
    Benchmark full-width to half-width conversion for voiced kana input.
    """
    s = ("バ" * 100) * BENCHMARK_REPEAT
    cnv = FullToHalfConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == ("ﾊﾞ" * 100) * BENCHMARK_REPEAT


def test_full_to_half_handakuon(benchmark):
    """
    Benchmark full-width to half-width conversion for semi-voiced kana input.
    """
    s = ("パ" * 100) * BENCHMARK_REPEAT
    cnv = FullToHalfConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == ("ﾊﾟ" * 100) * BENCHMARK_REPEAT


def test_full_to_half_halfwidth(benchmark):
    """
    Benchmark full-width to half-width conversion for already half-width input.
    """
    s = ("ﾊ" * 100) * BENCHMARK_REPEAT
    cnv = FullToHalfConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == ("ﾊ" * 100) * BENCHMARK_REPEAT


def test_hiragana_to_katakana(benchmark):
    """
    Benchmark hiragana to katakana conversion.
    """
    s = ("あ" * 100) * BENCHMARK_REPEAT
    cnv = HiraganaToKatakanaConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == ("ア" * 100) * BENCHMARK_REPEAT


def test_katakana_to_hiragana(benchmark):
    """
    Benchmark katakana to hiragana conversion.
    """
    s = ("ア" * 100) * BENCHMARK_REPEAT
    cnv = KatakanaToHiraganaConverter()
    actual = benchmark(cnv.convert, s)
    assert actual == ("あ" * 100) * BENCHMARK_REPEAT
