import logging
from pathlib import Path

import click

from stepbystep.routines.create import CreatorFactory

logger = logging.getLogger(__name__)


@click.command(help="creates a new routine in the --work_dir")
@click.help_option("--help", "-h")
@click.argument(
    "routine_name",
    type=str,
)
@click.option(
    "--work_dir",
    default=Path(),
    type=click.Path(exists=True, file_okay=False, dir_okay=True, resolve_path=False),
)
def add(routine_name, work_dir):
    work_dir = Path(work_dir)
    creator = CreatorFactory.get_creator(work_dir)
    creator.create(routine_name)
