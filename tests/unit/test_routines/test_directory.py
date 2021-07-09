from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path
import os

from click.exceptions import ClickException

from stepbystep.routines.constants import ROUTINES_DIR_NAME
from stepbystep.routines.directory import DirManager


class DirManagerTest(TestCase):
    def test_create(self):
        with TemporaryDirectory() as work_dir:
            work_dir = Path(work_dir)
            dir_manager = DirManager(work_dir=work_dir)

            routines_dir = dir_manager.get_path()
            self.assertFalse(routines_dir.exists())

            dir_manager.create()

            self.assertTrue(routines_dir.exists())

    def test_create_exists_already(self):
        with TemporaryDirectory() as work_dir:
            work_dir = Path(work_dir)
            dir_manager = DirManager(work_dir=work_dir)
            routines_dir = dir_manager.get_path()

            os.makedirs(routines_dir)
            self.assertTrue(routines_dir.exists())

            with self.assertRaises(ClickException):
                dir_manager.create()

            self.assertTrue(routines_dir.exists())
