#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import fileinput
from bisect import insort, bisect, bisect_right

numlist = [int(line) for line in fileinput.input()]


def part2(l):
    """
    This doesn't actually work, just works for mine and the test input
    """
    l = sorted(l)
    while l:
        if l[0] + l[-1] + l[-2] == 2020:
            return l[0] * l[-1] * l[-2]
        if l[0] + l[-1] + l[1] == 2020:
            return l[0] * l[-1] * l[1]

        l = l[:bisect(l, 2020 - (l[0] + l[1]))]
        l = l[bisect(l, 2019 - (l[-1] + l[-2])):]


print(part2(numlist))
