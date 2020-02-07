import unittest

from app import app
from count import count_values_in_multiple_str, count_values


class AppSuite(unittest.TestCase):

    def test_count_values_in_list(self):
        list = [
            '{"a":0, "b":0, "d":{"c": 1, "a":0}}',
            '{"a":0, "b":0, "d":{"c": 1, "a":0}}'
        ]
        self.assertEqual(10, count_values_in_multiple_str(list))

    def test_count_values_in_empty_list(self):
        list = []
        self.assertEqual(0, count_values_in_multiple_str(list))

    def test_count_values_in_empty_dict(self):
        list = ['{}']
        self.assertEqual(0, count_values_in_multiple_str(list))


if __name__ == '__main__':
    unittest.main()