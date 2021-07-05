import logging
from pathlib import Path

import click

from stepbystep.constants import ROUTINES_DIR_NAME

logger = logging.getLogger(__name__)


class Initializer:
    work_dir: Path

    def __init__(self, work_dir: Path):
        self.work_dir = work_dir

    def create_routines_dir(self):
        dest_dir = self.work_dir / ROUTINES_DIR_NAME
        if dest_dir.exists():
            pass


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
    initializer = Initializer(work_dir=work_dir)
    initializer.create_routines_dir()
