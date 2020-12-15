#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :


a = "2,1,10,11,0,6"


a = [int(b) for b in a.split(',')]


prev = None
m = {}
for i in range(30000000 - 1):
    if i < len(a):
        next_ = i - m.get(a[i], i)
        m[a[i]] = i
        continue
    say = next_
    next_ = i - m.get(say, i)
    m[say] = i


print(next_)
