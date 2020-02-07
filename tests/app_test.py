import unittest

import app


class AppSuite(unittest.TestCase):

    def test_a(self):
        self.assert_(False)


if __name__ == '__main__':
    unittest.main()