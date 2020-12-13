#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

a = """
1000303
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,541,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,983,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19
""".split()

b = int(a[0])
c = [int(d) if d.isdigit() else d for d in a[1].split(',') if d is not 'x']

print(b, c)

d = {(b / e) % 1: (e, (b // e)) for e in c}

f, g = d[max(d)]

print((f * (g + 1) - b) * f)
