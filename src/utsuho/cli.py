"""Module providing Utsuho's Command Line Interface (CLI)."""
import os.path

import click

from . import __version__
from .converters import FullToHalfConverter, HalfToFullConverter, HiraganaToKatakanaConverter, KatakanaToHiraganaConverter


@click.group(invoke_without_command=True)
@click.option('--version', is_flag=True, help='Show the version.')
@click.pass_context
def cli(ctx: click.Context, version: bool):
    """Utsuho is a Python module that facilitates bidirectional conversion
    between half-width katakana and full-width katakana in Japanese.
    Furthermore, it offers bidirectional conversion between hiragana and katakana.\f

    Parameters
    ----------
    ctx: click.Context
        Context for the click command.
    version: bool
        Whether to show the Utsuho version.
    """
    if version:
        click.echo(f'Utsuho {__version__}')
        ctx.exit()

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit()


@cli.command()
@click.option(
    '--file', '-f', 'file_', is_flag=True,
    help='Whether to use TEXT as a file path.'
)
@click.argument('text')
def full_to_half(file_: bool, text: str):
    """Convert from full-width to half-width characters.\f

    Parameters
    ----------
    file_: bool
        Whether to treat TEXT as a file path or not.
    text: str
        String containing characters to be converted to half-width characters or the path of a file containing them.
    """
    if file_:
        with open(os.path.abspath(text), 'r') as fp:
            s = fp.read()
    else:
        s = text

    cnv = FullToHalfConverter()
    converted = cnv.convert(s)
    click.echo(converted)


@cli.command()
@click.option(
    '--file', '-f', 'file_', is_flag=True,
    help='Whether to use TEXT as a file path.'
)
@click.argument('text')
def half_to_full(file_: bool, text: str):
    """Convert from half-width to full-width characters.\f

    Parameters
    ----------
    file_: bool
        Whether to treat TEXT as a file path or not.
    text: str
        String containing characters to be converted to full-width characters or the path of a file containing them.
    """
    if file_:
        with open(os.path.abspath(text), 'r') as fp:
            s = fp.read()
    else:
        s = text

    cnv = HalfToFullConverter()
    converted = cnv.convert(s)
    click.echo(converted)


@cli.command()
@click.option(
    '--file', '-f', 'file_', is_flag=True,
    help='Whether to use TEXT as a file path.'
)
@click.argument('text')
def hiragana_to_katakana(file_: bool, text: str):
    """Convert from hiragana to katakana.\f

    Parameters
    ----------
    file_: bool
        Whether to treat TEXT as a file path or not.
    text: str
        String containing characters to be converted to katakana or the path of a file containing them.
    """
    if file_:
        with open(os.path.abspath(text), 'r') as fp:
            s = fp.read()
    else:
        s = text

    cnv = HiraganaToKatakanaConverter()
    converted = cnv.convert(s)
    click.echo(converted)


@cli.command()
@click.option(
    '--file', '-f', 'file_', is_flag=True,
    help='Whether to use TEXT as a file path.'
)
@click.argument('text')
def katakana_to_hiragana(file_: bool, text: str):
    """Convert from katakana to hiragana.\f

    Parameters
    ----------
    file_: bool
        Whether to treat TEXT as a file path or not.
    text: str
        String containing characters to be converted to hiragana or the path of a file containing them.
    """
    if file_:
        with open(os.path.abspath(text), 'r') as fp:
            s = fp.read()
    else:
        s = text

    cnv = KatakanaToHiraganaConverter()
    converted = cnv.convert(s)
    click.echo(converted)
