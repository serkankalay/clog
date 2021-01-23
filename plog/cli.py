import logging

import click

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
)


@click.group()
def cli():
    "P(ersonal)log command-line interface."


@cli.command()
def hello() -> None:
    logger.info("Hello world.")
