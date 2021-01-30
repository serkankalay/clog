import logging

import click

from . import editor

logger = logging.getLogger(__name__)


@click.group()
def cli():
    "P(ersonal)log command-line interface."


@cli.command()
def hello() -> None:
    logger.info("Hello world.")


@cli.command()
def log() -> None:
    from_editor = editor.from_editor()
    logger.info(from_editor)
