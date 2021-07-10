import os

from click.testing import CliRunner

from stepbystep.routines.constants import ROUTINES_DIR_NAME
from stepbystep.commands.init import init
from tests.helpers import TempDirTest


class InitCommandTest(TempDirTest):
    def test_init(self):
        routines_dir = self.work_dir / ROUTINES_DIR_NAME
        self.assertFalse(routines_dir.exists())

        runner = CliRunner()
        result = runner.invoke(init, ["--work_dir", str(self.work_dir)])

        assert result.exit_code == 0
        assert "Initialized" in result.output
        self.assertTrue(routines_dir.exists())

    def test_init_exists_already(self):
        routines_dir = self.work_dir / ROUTINES_DIR_NAME
        os.makedirs(routines_dir)
        self.assertTrue(routines_dir.exists())

        runner = CliRunner()
        result = runner.invoke(init, ["--work_dir", str(self.work_dir)])

        assert result.exit_code == 1
        assert "subdirectory already exists in" in result.output
        self.assertTrue(routines_dir.exists())