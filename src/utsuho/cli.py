""" Utsuho's CLI (Command Line Interface).
"""
import os.path

import click

from . import __version__
from .converters import FullToHalfConverter, HalfToFullConverter


@click.group(invoke_without_command=True)
@click.option('--version', is_flag=True, help='Show version.')
@click.pass_context
def cli(ctx: click.Context, version: bool):
    """ Utsuho is an interconverter between Japanese half-width katakana and full-width katakana.\f

    Parameters
    ----------
    ctx: click.Context
        Context for click command.
    version: bool
        Whether to show Utsuho version.
    """
    if version:
        click.echo(f'Utsuho {__version__}')
        ctx.exit()

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit()


@cli.command()
@click.option('--file', '-f', 'file_', is_flag=True, help='Use TEXT as file path.')
@click.argument('text')
def full_to_half(file_: bool, text: str):
    """ Convert full-width katakana to half-width katakana.\f

    Parameters
    ----------
    file_: bool
        Whether to treat TEXT as a file path.
    text: str
        String containing characters to convert to half-width katakana or the path of file containing them.
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
@click.option('--file', '-f', 'file_', is_flag=True, help='Use TEXT as file path.')
@click.argument('text')
def half_to_full(file_: bool, text: str):
    """ Convert half-width katakana to full-width katakana.\f

    Parameters
    ----------
    file_: bool
        Whether to treat TEXT as a file path.
    text: str
        String containing characters to convert to full-width katakana or the path of file containing them.
    """
    if file_:
        with open(os.path.abspath(text), 'r') as fp:
            s = fp.read()
    else:
        s = text

    cnv = HalfToFullConverter()
    converted = cnv.convert(s)
    click.echo(converted)
