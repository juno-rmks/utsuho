"""
Tests for the utsuho.converters.config module.
"""

from utsuho.converters import WidthConverterConfig


class TestWidthConverterConfig:
    """
    Tests for the WidthConverterConfig class.
    """

    def test_default_config(self):
        """
        Verify that the default configuration values are set as expected.
        """
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

    def test_custom_config(self):
        """
        Verify that explicitly provided configuration values override defaults.
        """
        config = WidthConverterConfig(
            punctuation=False,
            ascii_digit=False,
        )

        assert not config.punctuation
        assert config.corner_brucket
        assert not config.ascii_digit
