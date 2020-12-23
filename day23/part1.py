#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

a = [5, 6, 2, 8, 9, 3, 1, 4, 7]


def move(a):
    # print(f'cups: {a}')
    current = a.pop(0)
    a.append(current)
    # print(f'current: {current}')
    c, d, e = (a.pop(0), a.pop(0), a.pop(0))
    # print(f'pick up: {c}, {d}, {e}')
    # print(f'cups after pickup: {a}')

    dest = current - 1
    while dest not in a:
        dest -= 1
        dest %= max(a) + 1
    # print(f'destination {dest}')
    dest_i = a.index(dest)
    a.insert(dest_i + 1, e)
    a.insert(dest_i + 1, d)
    a.insert(dest_i + 1, c)
    return a

# print(move(a, a[0]))

# print(move(a, 0))
# print(move(a, 1))
print(move([5, 4, 6, 7, 8, 9, 1, 3, 2]))

def iterate_compose(f, n):
    def wrap(arg):
        a = f(arg)
        for i in range(n - 1):
            a = f(arg)
        return a
    return wrap

print(iterate_compose(move, 100)(a))

