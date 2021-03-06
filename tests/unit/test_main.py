import unittest
import sys
from lore.util import suppress_stdout


class TestImport(unittest.TestCase):
    def test_import(self):
        # make sure this at least gets loaded
        import lore.__main__
        self.assertTrue(True)


class TestTask(unittest.TestCase):
    def test_task(self):
        import lore.__main__

        args = ('task', 'tests.mocks.tasks.EchoTask', '--arg1', 'true')
        with suppress_stdout():
            if sys.version_info[0] == 2:
                lore.__main__.main(args)
                self.assertTrue(True)
            else:
                with self.assertLogs('lore.__main__') as log:
                    lore.__main__.main(args)
                    self.assertEqual(log.output, [
                        "INFO:lore.__main__:starting task: " +
                        "tests.mocks.tasks.EchoTask {'arg1': 'true'}"
                    ])
