#!/usr/bin/env python3
"""Implementation of Burrows-Wheeler Transform"""
from pprint import pprint
DELIMITER = "$"


def extract(s):
    """Extract all rotations of a string"""
    s += DELIMITER
    # print(s)
    # create rotations
    rotations = [s[index:] + s[:index] for index in range(len(s))]
    rotations.sort()
    return list(enumerate(rotations))


def bwt(s: str):
    """The transform"""
    e = extract(s)
    final = ''.join(r[1][-1] for r in e)
    return final


def decode(encoded):
    """Inverse transform"""
    first = list(encoded)
    body = [[i] for i in first]
    body.sort()
    while len(body[0]) < len(encoded):
        for index, item in enumerate(first):
            body[index].insert(0, item)
        body.sort()
    return body


def bwti(encoded: str):

    return ''.join([i[:-1] for i in decode(encoded) if i[-1] == DELIMITER][0])


def main():
    tests = [
        "Hello, World!",
        "The quick brown fox jumped over the lazy dog.",
        "cool beans", ]
    for data in tests:
        t = bwt(data)
        print("bwt('{0}') # => {1}\nbwti('{1}')# => {2}".format(
            data, t,bwti(t)))
        print()


if __name__ == '__main__':
    main()
