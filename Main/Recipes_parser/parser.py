#!/usr/bin/python3

import json, pathlib

if __name__ == '__main__':
    path = (pathlib.Path(__file__).parents[2].joinpath('Tests', 'basic_test_data.txt'))
    print(path)
    with open(path, encoding='utf8') as json_file:
        database = json.load(json_file)
    print(database)
