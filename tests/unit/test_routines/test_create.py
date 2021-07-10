# from unittest import TestCase
# from tempfile import TemporaryDirectory
# from pathlib import Path
#
# from stepbystep.routines.directory import DirManager
# from stepbystep.routines.create import Creator
#
#
# class CreatorTest(TestCase):
#     def setUp(self) -> None:
#         self.temp_dir = TemporaryDirectory()
#         self.work_dir = Path(self.temp_dir.name)
#
#     def tearDown(self) -> None:
#         self.temp_dir.cleanup()
#
#     def test_assert_routines_dir_initialized(self):
#         with TemporaryDirectory() as work_dir:
#             work_dir = Path(work_dir)
#             dir_manager = DirManager(work_dir=work_dir)
#
