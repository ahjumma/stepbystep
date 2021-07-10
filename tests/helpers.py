from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path


class TempDirTest(TestCase):
    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()
        self.work_dir = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()
