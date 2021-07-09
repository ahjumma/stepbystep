import os
from abc import ABC, abstractmethod
from pathlib import Path

import click

from stepbystep.routines.constants import ROUTINES_DIR_NAME


class IDirManager(ABC):
    @abstractmethod
    def get_path(self) -> Path:
        pass

    @abstractmethod
    def create(self) -> None:
        pass


class DirManager(IDirManager):
    work_dir: Path

    def __init__(self, work_dir: Path) -> None:
        self.work_dir = work_dir

    def get_path(self) -> Path:
        return self.work_dir / ROUTINES_DIR_NAME

    def create(self) -> None:
        routines_dir = self.get_path()
        if routines_dir.exists():
            msg = f"{ROUTINES_DIR_NAME} subdirectory already exists in {self.work_dir} directory"
            raise click.ClickException(msg)
        else:
            os.makedirs(routines_dir)
            click.echo(
                f"Initialized {ROUTINES_DIR_NAME} subdirectory in {self.work_dir} directory"
            )


class DirManagerFactory:
    @classmethod
    def get_dir_manager(cls, work_dir: Path) -> IDirManager:
        return DirManager(work_dir=work_dir)
