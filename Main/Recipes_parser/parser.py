#!/usr/bin/python3

import json, pathlib, os

def parser():
    print(os.getcwd())
    path = pathlib.PurePath(pathlib.PurePath(os.getcwd()), 'Tests', 'basic_test_data.txt')
    print(path)
    with open(str(path), encoding='utf8') as json_file:
        database = json.load(json_file)
    return database


if __name__ == '__main__':
    testing = parser()
    #print(testing)
    value = testing.popitem()[1]
    for line in value:
        print((line))
    #path = (pathlib.Path(__file__).parents[2].joinpath('Tests', 'basic_test_data.txt'))
    #print(path)
    #with open(path, encoding='utf8') as json_file:
    #    database = json.load(json_file)
    #print(database)
