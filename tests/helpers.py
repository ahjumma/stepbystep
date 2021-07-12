from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, Callable, Optional
from unittest import TestCase


class TempDirTest(TestCase):
    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()
        self.work_dir = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()


def generate_mock_edit(
    user_input: Optional[str] = None,
) -> Callable[[Any], Optional[str]]:
    def mock_edit(*args, **kwargs) -> Optional[str]:
        return user_input

    return mock_edit
