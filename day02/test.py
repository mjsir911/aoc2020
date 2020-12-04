#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :


a = 0
with open("my.in") as file:
    for line in file:
        rule, password = line.strip().split(': ')
        r, char = rule.split(' ')
        start, end = r.split('-')
        start, end = int(start), int(end)
        valid = start <= password.count(char) <= end
        if valid:
            a += 1


print(a)

a  = 0
with open("my.in") as file:
    for line in file:
        rule, password = line.strip().split(': ')
        r, char = rule.split(' ')
        start, end = r.split('-')
        start, end = int(start), int(end)
        valid = False
        if (password[start - 1] == char) ^ (password[end - 1] == char):
            a += 1


print(a)

