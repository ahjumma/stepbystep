from unittest import TestCase

from click.testing import CliRunner

from stepbystep.main import main


class EntryMainTest(TestCase):
    def test_main_help(self):
        runner = CliRunner()
        result = runner.invoke(main, ["-h"])
        assert result.exit_code == 0
        assert "A cli tool for creating/managing" in result.output
