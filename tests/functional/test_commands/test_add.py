from unittest.mock import patch

from click.testing import CliRunner

from stepbystep.commands.add import add
from stepbystep.commands.init import init
from stepbystep.routines.constants import ROUTINES_DIR_NAME
from tests.helpers import TempDirTest, generate_mock_edit


class AddCommandTest(TempDirTest):
    def test_add_not_yet_initialized(self):
        routines_dir = self.work_dir / ROUTINES_DIR_NAME
        self.assertFalse(routines_dir.exists())

        runner = CliRunner()
        result = runner.invoke(
            add, ["new routine name", "--work_dir", str(self.work_dir)]
        )

        assert result.exit_code == 1
        assert "Routines directory has not been initialized yet" in result.output
        self.assertFalse(routines_dir.exists())

    def test_add(self):
        routines_dir = self.work_dir / ROUTINES_DIR_NAME
        self.assertFalse(routines_dir.exists())

        runner = CliRunner()
        runner.invoke(init, ["--work_dir", str(self.work_dir)])

        user_input = "This is a new message"
        mock_edit = generate_mock_edit(user_input)
        routine_name = "new routine name"
        with patch("click.edit", mock_edit):
            result = runner.invoke(
                add, [routine_name, "--work_dir", str(self.work_dir)]
            )

        assert result.exit_code == 0
        assert "Created a new routine named" in result.output
        self.assertTrue(routines_dir.exists())

        routine_path = routines_dir / routine_name
        with open(routine_path, "r") as f:
            data = f.read()
        self.assertIn(user_input, data)

    # def test_init_exists_already(self):
    #     routines_dir = self.work_dir / ROUTINES_DIR_NAME
    #     os.makedirs(routines_dir)
    #     self.assertTrue(routines_dir.exists())
    #
    #     runner = CliRunner()
    #     result = runner.invoke(init, ["--work_dir", str(self.work_dir)])
    #
    #     assert result.exit_code == 1
    #     assert "subdirectory already exists in" in result.output
    #     self.assertTrue(routines_dir.exists())
