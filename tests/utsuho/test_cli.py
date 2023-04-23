from click.testing import CliRunner

from utsuho import __version__
from utsuho.cli import cli


def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(cli, [])
    assert 'Usage: cli [OPTIONS] COMMAND [ARGS]...' in result.output
    assert result.exit_code == 0

    result = runner.invoke(cli, ['--help'])
    assert 'Usage: cli [OPTIONS] COMMAND [ARGS]...' in result.output
    assert result.exit_code == 0


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(cli, ['--version'])
    assert result.output == f'Utsuho {__version__}\n'
    assert result.exit_code == 0


def test_cli_full_to_half():
    runner = CliRunner()
    result = runner.invoke(cli, ['full-to-half', 'キョウトシ　サキョウク　ギンカクジチョウ　２'])
    assert result.output == 'ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2\n'
    assert result.exit_code == 0


def test_cli_full_to_half_with_filepath():
    runner = CliRunner()

    with runner.isolated_filesystem():
        with open('test_full.txt', 'w') as fp:
            fp.write('キョウトシ　サキョウク　ギンカクジチョウ　２')

        result = runner.invoke(cli, ['full-to-half', '--file', 'test_full.txt'])
        assert result.output == 'ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2\n'
        assert result.exit_code == 0


def test_cli_full_to_half_without_filepath():
    runner = CliRunner()
    result = runner.invoke(cli, ['full-to-half', 'test_full.txt'])
    assert result.output == 'test_full.txt\n'
    assert result.exit_code == 0


def test_cli_half_to_full():
    runner = CliRunner()
    result = runner.invoke(cli, ['half-to-full', 'ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2'])
    assert result.output == 'キョウトシ　サキョウク　ギンカクジチョウ　２\n'
    assert result.exit_code == 0


def test_cli_half_to_full_with_filepath():
    runner = CliRunner()

    with runner.isolated_filesystem():
        with open('test_half.txt', 'w') as fp:
            fp.write('ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2')

        result = runner.invoke(cli, ['half-to-full', '--file', 'test_half.txt'])
        assert result.output == 'キョウトシ　サキョウク　ギンカクジチョウ　２\n'
        assert result.exit_code == 0


def test_cli_half_to_full_without_filepath():
    runner = CliRunner()
    result = runner.invoke(cli, ['half-to-full', 'test_half.txt'])
    assert result.output == 'ｔｅｓｔ＿ｈａｌｆ．ｔｘｔ\n'
    assert result.exit_code == 0
