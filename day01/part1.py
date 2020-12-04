#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import fileinput
from bisect import insort, bisect, bisect_right

numlist = [int(line) for line in fileinput.input()]
numlist = sorted(numlist)


def part1(l):
    while l:
        if l[0] + l[-1] == 2020:
            return l[0] * l[-1]
        l = l[:bisect(l, 2020 - l[0])]
        l = l[bisect(l, 2019 - l[-1]):]


print(part1(numlist))
# from timeit import timeit
# print(timeit('part1(numlist)', globals=globals(), number=100000))
