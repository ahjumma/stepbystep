from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path
import os

from click.exceptions import ClickException

from stepbystep.constants import ROUTINES_DIR_NAME
from stepbystep.commands.init import Initializer


class InitializerTest(TestCase):
    def test_create_routines_dir(self):
        with TemporaryDirectory() as work_dir:
            work_dir = Path(work_dir)
            initializer = Initializer(work_dir=work_dir)

            routines_dir = work_dir / ROUTINES_DIR_NAME
            self.assertFalse(routines_dir.exists())

            initializer.create_routines_dir()

            self.assertTrue(routines_dir.exists())

    def test_create_routines_dir_exists_already(self):
        with TemporaryDirectory() as work_dir:
            work_dir = Path(work_dir)
            initializer = Initializer(work_dir=work_dir)
            routines_dir = work_dir / ROUTINES_DIR_NAME

            os.makedirs(routines_dir)
            self.assertTrue(routines_dir.exists())

            with self.assertRaises(ClickException):
                initializer.create_routines_dir()

            self.assertTrue(routines_dir.exists())
