import logging

import click

logger = logging.getLogger(__name__)


@click.group()
def cli():
    "P(ersonal)log command-line interface."


@cli.command()
def hello() -> None:
    logger.info("Hello world.")
