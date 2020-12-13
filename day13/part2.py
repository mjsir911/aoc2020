#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

a = """
1000303
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,541,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,983,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19
""".split()

# a = """
# 939
# 7,13,x,x,59,x,31
# """.split()

b = int(a[0])
c = [int(d) if d.isdigit() else d for d in a[1].split(',')]


def d(c):
    return {g: i for i, g in enumerate(c) if g is not 'x'}


def e(i, modmap):
    return {k: (i + n) % k for k, n in modmap.items()}


def test(i, modmap):
    return all(v == 0 for v in e(i, modmap).values())


def test2(n, m, i):
    return int((1 + (m * n)) * i)

from decimal import Decimal
# print(test2(51, (Decimal(10087) / 4718) - 1, 4718))
# exit()


def brute(d, inc=1):
    from itertools import count
    for i in count(step=inc):
        if test(i, d):
            return i

# print('answer:', brute(d(c), inc=13))


diff = 1
i = 0
base = None
precision = 1
while True:
    if test(i, d(c[:precision])):
        if base is None:
            base = i
            print(f'base is: {base}, diff is {diff}')
            if test(i, d(c)):
              break
        else:
            # print(f'next is {i}')
            diff = (i - base)
            precision += 1
            base = None
            continue

    i += diff

    # print(i)

print(base)

from itertools import count
from math import sqrt
# for i in range(3269660113287150, 0, -1):
#     print(i)
#     if test(i, d(c)):
#         print(i)

# this is for printing into wolfram alpha
# for a, b in d(c).items():
#     print(f'((n + {b}) mod {a}) and ', end='')
# print()
# print(d(c))
