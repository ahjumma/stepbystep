import logging
from pathlib import Path

import click

from stepbystep.routines.directory import DirManagerFactory

logger = logging.getLogger(__name__)


@click.command(
    help="creates a subdirectory in --work_dir where routine files will be created and read from"
)
@click.help_option("--help", "-h")
@click.option(
    "--work_dir",
    default=Path(),
    type=click.Path(exists=True, file_okay=False, dir_okay=True, resolve_path=False),
)
def init(work_dir):
    work_dir = Path(work_dir)
    dir_manager = DirManagerFactory.get_dir_manager(work_dir)
    dir_manager.create()
