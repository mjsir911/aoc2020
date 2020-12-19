#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

a, z = open('my.in').read().strip().split('\n\n')
a = a.split('\n')
z = z.split('\n')

class Or(tuple):
    def __repr__(self):
        return f'Or{super().__repr__()}'

    def to_regex(self):
        if len(self) == 1:
            return self[0].to_regex()
        return '(' + '|'.join(c.to_regex() for c in self)  + ')'


class And(tuple):
    def __repr__(self):
        return f'And({super().__repr__()})'

    def to_regex(self):
        if len(self) == 1:
            return self[0].to_regex()
        return '(' + ''.join(c.to_regex() for c in self) + ')'


class Char(str):
    def __repr__(self):
        return f'Char{super().__repr__()}'

    def to_regex(self):
        return self


d = {}
for c in a:
    if not c:
        continue
    t, y = c.split(': ')
    d[int(t)] = Or(And(int(f) if f.isdigit() else Char(eval(f)) for f in b.split(" ")) for b in y.split(" | "))


def expand(d, r):
    if isinstance(r, str):
        return r
    return Or(And(expand(d, d[v]) if v in d else v for v in or_p) for or_p in r)



import re
f = expand(d, d[0])
r = re.compile('^' + f.to_regex() + '$')

acc = 0
print(r)
for y in z:
    if r.match(y):
        acc += 1

print(acc)
# # print(f('ababbb'))
