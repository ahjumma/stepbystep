import os

from click.exceptions import ClickException

from stepbystep.routines.directory import DirManager
from tests.helpers import TempDirTest


class DirManagerTest(TempDirTest):
    def test_create(self):
        dir_manager = DirManager(work_dir=self.work_dir)

        routines_dir = dir_manager.get_path()
        self.assertFalse(routines_dir.exists())

        dir_manager.create()

        self.assertTrue(routines_dir.exists())

    def test_create_exists_already(self):
        dir_manager = DirManager(work_dir=self.work_dir)
        routines_dir = dir_manager.get_path()

        os.makedirs(routines_dir)
        self.assertTrue(routines_dir.exists())

        with self.assertRaises(ClickException):
            dir_manager.create()

        self.assertTrue(routines_dir.exists())
