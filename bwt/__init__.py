#!/usr/bin/env python3
"""Implementation of Burrows-Wheeler Transform"""
from pprint import pprint
DELIMITER = "$"


def extract(s):
    """Extract all rotations of a string"""
    s = s + DELIMITER
    # create rotations
    rotations = [s[index:] + s[:index] for index in range(len(s))]
    rotations.sort()
    return list(enumerate(rotations))


def bwt(s: str):
    """The transform"""
    final = ''.join(r[1][-1] for r in extract(s))
    return final


def decode(encoded):
    """Inverse transform"""
    first = list(encoded)
    body = [[i] for i in first]
    body.sort()
    didx = [index for index, item in enumerate(
        body) if item[-1] == DELIMITER][0]
    linear = [body[didx][-1]]
    while len(body[0]) < len(encoded):
        for index, item in enumerate(first):
            body[index].insert(0, item)
        body.sort()
    return body


def bwti(encoded: str):

    return ''.join([i[:-1] for i in decode(encoded) if i[-1] == DELIMITER][0])


def main():
    data = "Hello, World!"
    data = "cool beans"
    data = "The quick brown fox jumped over the lazy dog."
    data = "count character occurences"
    t = bwt(data)
    print(data)
    print(t)
    pprint(bwti(t))


if __name__ == '__main__':
    main()
