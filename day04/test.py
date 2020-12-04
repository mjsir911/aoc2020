#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import string
from sys import stdin
from string import hexdigits

a = stdin.read().split("\n\n")

valid_fields = "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
a = [a.replace("\n", " ").strip() for a in a]

c = 0
for passport in a:
    passport = passport.split(" ")
    fields = {s[:s.find(":")]: s[s.find(":") + 1:] for s in passport}
    valid = True
    locals().update(fields)
    if set(valid_fields) - set(fields):
        print('a')
        continue
    if not (1920 <= int(byr) <= 2002):
        print('b')
        continue
    if not (2010 <= int(iyr) <= 2020):
        print('c')
        continue
    if not (2020 <= int(eyr) <= 2030):
        print('d')
        continue
    if hgt.endswith('cm'):
        if not 150 <= int(hgt[:-2]) <= 193:
            print('e')
            continue
    elif hgt.endswith('in'):
        if not 59 <= int(hgt[:-2]) <= 76:
            print('f')
            continue
    else:
        print('g')
        continue
    if not hcl.startswith('#'):
        print('h')
        continue
    if not all(c in string.hexdigits for c in hcl[1:]):
        print('i')
        continue
    if ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        print('j')
        continue
    if len(pid) != 9:
        print('k')
        continue
    if not pid.isdigit():
        print('l')
        continue
    c += 1
print(c)
