"""
Command-line interface for Utsuho.
"""

import os.path

import click

from . import __version__
from .converters import (
    FullToHalfConverter,
    HalfToFullConverter,
    HiraganaToKatakanaConverter,
    KatakanaToHiraganaConverter,
)


def _read_input_text(file_: bool, text: str | None) -> str:
    """
    Resolve input text from argument, file, or stdin.

    Parameters
    ----------
    file_ : bool
        Whether to treat TEXT as a file path or not.
    text : str | None
        String containing characters to be converted or the path of a file
        containing them.

    Returns
    -------
    str
        The resolved input text.
    """
    if file_ and text is None:
        raise click.UsageError("TEXT argument is required when using --file.")

    if text is None:
        if click.get_text_stream("stdin").isatty():
            raise click.UsageError("TEXT argument is required when stdin is not piped.")

        text = click.get_text_stream("stdin").read()

        if text == "":
            raise click.UsageError("No input was provided via stdin.")

    if file_:
        with open(os.path.abspath(text), "r", encoding="utf-8") as fp:
            return fp.read()

    return text


@click.group(invoke_without_command=True)
@click.option(
    "--version",
    is_flag=True,
    help="Show the version.",
)
@click.pass_context
def cli(
    ctx: click.Context,
    version: bool,
):
    """
    Utsuho provides deterministic normalization utilities for Japanese text,
    including width normalization and hiragana/katakana conversion.\f

    Parameters
    ----------
    ctx : click.Context
        Context for the click command.
    version : bool
        Whether to show the Utsuho version.
    """
    if version:
        click.echo(f"Utsuho {__version__}")
        ctx.exit()

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit()


@cli.command()
@click.option(
    "--file",
    "-f",
    "file_",
    is_flag=True,
    help="Whether to use TEXT as a file path.",
)
@click.argument("text", required=False)
def full_to_half(
    file_: bool,
    text: str | None,
):
    """
    Convert from full-width to half-width characters.\f

    Parameters
    ----------
    file_ : bool
        Whether to treat TEXT as a file path or not.
    text : str | None
        String containing characters to be converted to half-width characters
        or the path of a file containing them.
    """
    s = _read_input_text(file_, text)

    cnv = FullToHalfConverter()
    converted = cnv.convert(s)
    click.echo(converted)


@cli.command()
@click.option(
    "--file",
    "-f",
    "file_",
    is_flag=True,
    help="Whether to use TEXT as a file path.",
)
@click.argument("text", required=False)
def half_to_full(
    file_: bool,
    text: str | None,
):
    """
    Convert from half-width to full-width characters.\f

    Parameters
    ----------
    file_ : bool
        Whether to treat TEXT as a file path or not.
    text : str | None
        String containing characters to be converted to full-width characters
        or the path of a file containing them.
    """
    s = _read_input_text(file_, text)

    cnv = HalfToFullConverter()
    converted = cnv.convert(s)
    click.echo(converted)


@cli.command()
@click.option(
    "--file",
    "-f",
    "file_",
    is_flag=True,
    help="Whether to use TEXT as a file path.",
)
@click.argument("text", required=False)
def hiragana_to_katakana(
    file_: bool,
    text: str | None,
):
    """
    Convert from hiragana to katakana.\f

    Parameters
    ----------
    file_ : bool
        Whether to treat TEXT as a file path or not.
    text : str | None
        String containing characters to be converted to katakana or the path of
        a file containing them.
    """
    s = _read_input_text(file_, text)

    cnv = HiraganaToKatakanaConverter()
    converted = cnv.convert(s)
    click.echo(converted)


@cli.command()
@click.option(
    "--file",
    "-f",
    "file_",
    is_flag=True,
    help="Whether to use TEXT as a file path.",
)
@click.argument("text", required=False)
def katakana_to_hiragana(
    file_: bool,
    text: str | None,
):
    """
    Convert from katakana to hiragana.\f

    Parameters
    ----------
    file_ : bool
        Whether to treat TEXT as a file path or not.
    text : str | None
        String containing characters to be converted to hiragana or the path of
        a file containing them.
    """
    s = _read_input_text(file_, text)

    cnv = KatakanaToHiraganaConverter()
    converted = cnv.convert(s)
    click.echo(converted)
