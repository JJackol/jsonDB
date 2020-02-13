import pytest
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
         (list_in_json, 4),
         (empty_list, 0)
         ]

invalid_jsons = [
    ['xxx'],
    ['{"a":0, "b":0, "d":0'],
    ['{a:0, "b":0, "d":0}'],
    ['{"a":0, "b:0, "d":0}'],
    ['{"a":0, "b":0, "d":0}', '{"a":0 "b":0, "d":0}']
]


@pytest.mark.parametrize("list,expect", pairs)
def test_count_values_in_list(list, expect):
    assert expect == (count_values_in_multiple_str(list))

def test_count_values_in_empty_list():
    list = []
    assert 0 == count_values_in_multiple_str(list)

def test_count_values_in_empty_dict():
    list = ['{}']
    assert 0 == count_values_in_multiple_str(list)

@pytest.mark.parametrize("json", invalid_jsons)
def test_count_values_exceptions_expected(json):
    with pytest.raises(Exception):
        count_values_in_multiple_str(json)


