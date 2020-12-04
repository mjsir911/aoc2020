#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import fileinput

a = [l.strip() for l in fileinput.input()]


def slope(a, right, down):
    c = 0
    x = 0
    y = 0
    for i in range(0, len(a) - 1, down):
        x += down
        y += right
        if a[x][y % len(a[0])] == "#":
            c += 1
    return c


print(slope(a, 3, 1))

c = 0

x = 0
y = 0


print(slope(a, 1, 1) * slope(a, 3, 1) * slope(a, 5, 1) * slope(a, 7, 1) * slope(a, 1, 2))
