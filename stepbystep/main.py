# Copyright 2021 Andrew Kim
# Licensed under the MIT license

import logging

import click

from stepbystep import __version__
from stepbystep.commands.init import init

logger = logging.getLogger(__name__)


@click.group(
    help="A cli tool for creating/managing systematic routines to guide humans step-by-step"
)
@click.help_option("--help", "-h")
@click.version_option(__version__, "--version", "-V", prog_name="stepbystep")
def main():
    pass


main.add_command(init)


if __name__ == "__main__":
    main()
