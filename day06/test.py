#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

from sys import stdin
from string import ascii_lowercase
from functools import reduce

b = stdin.read().split("\n\n")
b = [[set(c) for c in a.strip().split()] for a in b]


def part1(b):
    return sum(len(reduce(set.union, i)) for i in b)


print(part1(b))


def part2(b):
    return sum(len(reduce(set.intersection, i)) for i in b)


print(part2(b))
