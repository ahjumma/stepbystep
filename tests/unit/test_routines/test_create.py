from pathlib import Path
from typing import Optional
from unittest.mock import Mock, patch

import click

# from stepbystep.routines.directory import DirManager
from stepbystep.routines.create import Creator
from tests.helpers import TempDirTest


class CreatorTest(TempDirTest):
    def test_assert_routines_dir_initialized(self):
        dir_manager = Mock()
        dir_manager.get_path.return_value = self.work_dir
        creator = Creator(dir_manager=dir_manager)

        creator._assert_routines_dir_initialized()

    def test_assert_routines_dir_initialized_negative(self):
        invalid_dir = "a random directory name"
        dir_manager = Mock()
        dir_manager.get_path.return_value = Path(invalid_dir)
        creator = Creator(dir_manager=dir_manager)

        with self.assertRaises(click.exceptions.ClickException):
            creator._assert_routines_dir_initialized()

    def test_assert_routine_not_exists(self):
        dir_manager = Mock()
        dir_manager.get_path.return_value = self.work_dir
        creator = Creator(dir_manager=dir_manager)

        routine_name = "how to brush your teeth"
        creator._assert_routine_not_exists(routine_name)

    def test_assert_routine_not_exists_negative(self):
        routine_name = "how to brush your teeth"
        routine_path = self.work_dir / routine_name
        with open(routine_path, "w") as f:
            f.write("stub data")

        dir_manager = Mock()
        dir_manager.get_path.return_value = self.work_dir
        creator = Creator(dir_manager=dir_manager)

        with self.assertRaises(click.exceptions.ClickException):
            creator._assert_routine_not_exists(routine_name)

    def test_build_routine_path(self):
        routine_name = "how to brush your teeth"
        expected_path = self.work_dir / routine_name

        dir_manager = Mock()
        dir_manager.get_path.return_value = self.work_dir
        creator = Creator(dir_manager=dir_manager)

        routine_path = creator._build_routine_path(routine_name)
        self.assertEqual(routine_path, expected_path)

    def test_load_initial_data(self):
        creator = Creator(dir_manager=Mock())

        data = creator._load_initial_data()

        first_line = data.split()[0]
        expected_line = "#" * 80
        self.assertEqual(first_line, expected_line)

    def test_create_routine(self):
        dir_manager = Mock()
        dir_manager.get_path.return_value = self.work_dir
        creator = Creator(dir_manager=dir_manager)

        def mock_edit(*args, **kwargs) -> Optional[str]:
            return "hello"

        routine_name = "how to brush your teeth"
        with patch("click.edit", mock_edit):
            created = creator._create_routine(routine_name)

        self.assertTrue(created)
        routine_path = creator._build_routine_path(routine_name)
        self.assertTrue(routine_path.exists())

    def test_create_routine_cancelled(self):
        dir_manager = Mock()
        dir_manager.get_path.return_value = self.work_dir
        creator = Creator(dir_manager=dir_manager)

        def mock_edit(*args, **kwargs) -> Optional[str]:
            return None

        routine_name = "how to brush your teeth"
        with patch("click.edit", mock_edit):
            created = creator._create_routine(routine_name)

        self.assertFalse(created)
        routine_path = creator._build_routine_path(routine_name)
        self.assertFalse(routine_path.exists())

    def test_create(self):
        dir_manager = Mock()
        dir_manager.get_path.return_value = self.work_dir
        creator = Creator(dir_manager=dir_manager)

        def mock_edit(*args, **kwargs) -> Optional[str]:
            return "hello"

        routine_name = "how to brush your teeth"
        with patch("click.edit", mock_edit):
            creator.create(routine_name)

        routine_path = creator._build_routine_path(routine_name)
        self.assertTrue(routine_path.exists())

    def test_create_cancelled(self):
        dir_manager = Mock()
        dir_manager.get_path.return_value = self.work_dir
        creator = Creator(dir_manager=dir_manager)

        def mock_edit(*args, **kwargs) -> Optional[str]:
            return None

        routine_name = "how to brush your teeth"
        with patch("click.edit", mock_edit):
            creator.create(routine_name)

        routine_path = creator._build_routine_path(routine_name)
        self.assertFalse(routine_path.exists())
