from abc import ABC, abstractmethod
from pathlib import Path

import click

from stepbystep.routines.constants import INITIAL_TEMPLATE_PATH
from stepbystep.routines.directory import DirManager


class ICreator(ABC):
    @abstractmethod
    def create(self, routine_name: str) -> None:
        pass


class Creator(ICreator):
    dir_manager: DirManager

    def __init__(self, dir_manager: DirManager) -> None:
        self.dir_manager = dir_manager

    def create(self, routine_name: str) -> None:
        self._assert_routines_dir_initialized()
        self._assert_routine_not_exists(routine_name)

    def _assert_routines_dir_initialized(self) -> None:
        routines_dir = self.dir_manager.get_path()
        if not routines_dir.exists():
            msg = "Routines directory has not been initialized yet"
            raise click.ClickException(msg)

    def _assert_routine_not_exists(self, routine_name: str) -> None:
        routine_path = self._build_routine_path(routine_name)
        if routine_path.exists():
            msg = "Routines directory has not been initialized yet"
            raise click.ClickException(msg)

    def _build_routine_path(self, routine_name: str) -> Path:
        routines_dir = self.dir_manager.get_path()
        routine_path = routines_dir / routine_name
        return routine_path

    def _create_routine(self, routine_name: str) -> None:
        routine_path = self._build_routine_path(routine_name)
        initial_data = self._load_initial_data()
        edited_data = click.edit(initial_data)
        with open(routine_path, "w") as f:
            f.write(edited_data)

    def _load_initial_data(self) -> str:
        with open(INITIAL_TEMPLATE_PATH, "r") as f:
            return f.read()
