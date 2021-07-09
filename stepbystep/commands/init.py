import logging
import os
from pathlib import Path

import click

from stepbystep.constants import ROUTINES_DIR_NAME

logger = logging.getLogger(__name__)


class Initializer:
    work_dir: Path

    def __init__(self, work_dir: Path):
        self.work_dir = work_dir

    def create_routines_dir(self):
        dest_dir = self._get_dest_dir()
        if dest_dir.exists():
            click.echo(
                f"{ROUTINES_DIR_NAME} subdirectory already exists in {self.work_dir} directory"
            )
            raise click.Abort()
        else:
            os.makedirs(dest_dir)
            click.echo(
                f"Initialized {ROUTINES_DIR_NAME} subdirectory in {self.work_dir} directory"
            )

    def _get_dest_dir(self):
        return self.work_dir / ROUTINES_DIR_NAME


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
    initializer = Initializer(work_dir=Path(work_dir))
    initializer.create_routines_dir()
