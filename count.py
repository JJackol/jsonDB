
from flask import json

def count_values_in_multiple_str(list):
    count = 0
    for j in list:
        count += count_values( json.loads(j) )
    return count

def count_values(dict):
    count = 0
    for k, v in dict.items():
        if type(v) == type({}):
            count += count_values(v)
    return count + len(dict)

list = [
    '{"a":0, "b":0, "d":{"c": 1, "a":0}}',
    '{"a":0, "b":0, "d":{"c": 1, "a":0}}'
]
#print(count_values(json.loads(list[0])))
#print(len(json.loads(list[0]).keys()))
#print(count_values_in_multiple_str(list))
#print(type({}))

