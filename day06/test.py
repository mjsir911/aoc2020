#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

from sys import stdin
from string import ascii_lowercase

b = stdin.read().split("\n\n")
b = [set(c for c in a.strip().split()) for a in b]


def part1(b):
    c = 0
    for i in b:
        i = {g for h in i for g in h}
        c += len(i)
    return c


print(part1(b))


def part2(b):
    from functools import reduce
    c = 0
    for i in b:
        c += len(reduce(set.intersection, [set(c) for c in i]))
    return c


print(part2(b))
