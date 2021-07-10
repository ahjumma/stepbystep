from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase


class TempDirTest(TestCase):
    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()
        self.work_dir = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()
