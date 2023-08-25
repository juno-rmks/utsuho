from utsuho.converters import WidthConverterConfig


def test_default_config():
    config = WidthConverterConfig()
    assert config.punctuation
    assert config.corner_brucket
    assert config.conjunction_mark
    assert config.length_mark
    assert config.space
    assert config.ascii_symbol
    assert config.ascii_alphabet
    assert config.ascii_digit
    assert not config.wave_dash
