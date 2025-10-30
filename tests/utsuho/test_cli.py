"""
Tests for the Utsuho command-line interface (CLI).
"""

from click.testing import CliRunner

from utsuho import __version__
from utsuho.cli import cli


def test_cli_no_arguments_shows_help():
    """
    Shows help text when no arguments or subcommands are passed.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [])
    assert (
        "Utsuho is a Python module that facilitates bidirectional conversion between"
        in result.output
    )
    assert result.exit_code == 0


def test_cli_option_help_shows_help():
    """
    Shows help text when the `--help` option is passed.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert (
        "Utsuho is a Python module that facilitates bidirectional conversion between"
        in result.output
    )
    assert result.exit_code == 0


def test_cli_option_version_shows_version():
    """
    Displays the correct version string when the `--version` option is passed.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.output == f"Utsuho {__version__}\n"
    assert result.exit_code == 0


def test_cli_full_to_half():
    """
    Converts full-width text to half-width text.
    """
    runner = CliRunner()
    result = runner.invoke(
        cli, ["full-to-half", "キョウトシ　サキョウク　ギンカクジチョウ　２"]
    )
    assert result.output == "ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2\n"
    assert result.exit_code == 0


def test_cli_full_to_half_with_file():
    """
    Converts full-width text to half-width text using an input file.
    """
    runner = CliRunner()

    with runner.isolated_filesystem():
        with open("test_full.txt", "w", encoding="utf-8") as fp:
            fp.write("キョウトシ　サキョウク　ギンカクジチョウ　２")

        result = runner.invoke(cli, ["full-to-half", "--file", "test_full.txt"])
        assert result.output == "ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2\n"
        assert result.exit_code == 0


def test_cli_full_to_half_without_file():
    """
    Outputs the raw string if the input is not a valid file path.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["full-to-half", "test_full.txt"])
    assert result.output == "test_full.txt\n"
    assert result.exit_code == 0


def test_cli_half_to_full():
    """
    Converts half-width text to full-width text.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["half-to-full", "ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2"])
    assert result.output == "キョウトシ　サキョウク　ギンカクジチョウ　２\n"
    assert result.exit_code == 0


def test_cli_half_to_full_with_file():
    """
    Converts half-width text to full-width text using an input file.
    """
    runner = CliRunner()

    with runner.isolated_filesystem():
        with open("test_half.txt", "w", encoding="utf-8") as fp:
            fp.write("ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2")

        result = runner.invoke(cli, ["half-to-full", "--file", "test_half.txt"])
        assert result.output == "キョウトシ　サキョウク　ギンカクジチョウ　２\n"
        assert result.exit_code == 0


def test_cli_half_to_full_without_file():
    """
    Outputs the raw string if the input is not a valid file path.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["half-to-full", "test_half.txt"])
    assert result.output == "ｔｅｓｔ＿ｈａｌｆ．ｔｘｔ\n"
    assert result.exit_code == 0


def test_cli_hiragana_to_katakana():
    """
    Converts hiragana text to katakana text.
    """
    runner = CliRunner()
    result = runner.invoke(
        cli, ["hiragana-to-katakana", "きょうとし　さきょうく　ぎんかくじちょう　２"]
    )
    assert result.output == "キョウトシ　サキョウク　ギンカクジチョウ　２\n"
    assert result.exit_code == 0


def test_cli_hiragana_to_katakana_with_file():
    """
    Converts hiragana text to katakana text using an input file.
    """
    runner = CliRunner()

    with runner.isolated_filesystem():
        with open("test_hiragana.txt", "w", encoding="utf-8") as fp:
            fp.write("きょうとし　さきょうく　ぎんかくじちょう　２")

        result = runner.invoke(
            cli, ["hiragana-to-katakana", "--file", "test_hiragana.txt"]
        )
        assert result.output == "キョウトシ　サキョウク　ギンカクジチョウ　２\n"
        assert result.exit_code == 0


def test_cli_hiragana_to_katakana_without_file():
    """
    Outputs the raw string if the input is not a valid file path.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["hiragana-to-katakana", "test_hiragana.txt"])
    assert result.output == "test_hiragana.txt\n"
    assert result.exit_code == 0


def test_cli_katakana_to_hiragana():
    """
    Converts katakana text to hiragana text.
    """
    runner = CliRunner()
    result = runner.invoke(
        cli, ["katakana-to-hiragana", "キョウトシ　サキョウク　ギンカクジチョウ　２"]
    )
    assert result.output == "きょうとし　さきょうく　ぎんかくじちょう　２\n"
    assert result.exit_code == 0


def test_cli_katakana_to_hiragana_with_file():
    """
    Converts katakana text to hiragana text using an input file.
    """
    runner = CliRunner()

    with runner.isolated_filesystem():
        with open("test_katakana.txt", "w", encoding="utf-8") as fp:
            fp.write("キョウトシ　サキョウク　ギンカクジチョウ　２")

        result = runner.invoke(
            cli, ["katakana-to-hiragana", "--file", "test_katakana.txt"]
        )
        assert result.output == "きょうとし　さきょうく　ぎんかくじちょう　２\n"
        assert result.exit_code == 0


def test_cli_katakana_to_hiragana_without_file():
    """
    Outputs the raw string if the input is not a valid file path.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["katakana-to-hiragana", "test_katakana.txt"])
    assert result.output == "test_katakana.txt\n"
    assert result.exit_code == 0
