import pytest
import unittest
from src.count import *

empty_json = ['{}']
nested_jsons1 = [
    '{"a":0, "b":0, "d":{"c": 1, "a":0}}'
]
nested_jsons2 = [
    '{"a":0, "b":0, "d":{"c": 1, "a":0}}',
    '{"x":0, "y":0, "z":{"c": 1, "a":0}}'
]
nested_jsons3 = [
    '{"a":0, "b":0, "d":{"c": 1, "a":0}}',
    '{"a":0, "b":0, "d":0}'
]
list_in_json = [
    '{"a":[{"a":0, "b":0, "d":0},{"a":0, "b":0, "d":0}]}',
    '{"a":0, "b":0, "d":0}'
]
empty_list = []

pairs = [(empty_json, 0),
         (nested_jsons1, 5),
         (nested_jsons2, 10),
         (nested_jsons3, 8),
         (list_in_json, 9+3)
         ]

invalid_json = ['xxx']


@pytest.mark.parametrize("list,expect", pairs)
def test_count_values_in_list(list, expect):
    assert expect == (count_values_in_multiple_str(list))


def test_count_values_in_empty_list():
    list = []
    assert 0 == count_values_in_multiple_str(list)

def test_count_values_in_empty_dict():
    list = ['{}']
    assert 0  == count_values_in_multiple_str(list)


