import unittest


class MockTestCase(unittest.TestCase):
    def test_module_is_reacting_as_the_legacy_module(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
