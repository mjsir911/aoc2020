#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import fileinput

numlist = [int(line) for line in fileinput.input()]


for i, num1 in enumerate(numlist):
    for j, num2 in enumerate(numlist[i:], start=i):
        if num1 + num2 == 2020:
            return num1 * num2


for i, num1 in enumerate(numlist):
    for j, num2 in enumerate(numlist[i:], start=i):
        for k, num3 in enumerate(numlist[j:], start=j):
            if num1 + num2 + num3 == 2020:
                print(num1 * num2 * num3)
