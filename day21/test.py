#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

a = open('my.in').read().split('\n')
for line in a:
    if not line:
        continue
    foods, allergens = line.split('(contains ')
    allergens = allergens[:-1].split(', ')
    foods = foods[:-1].split(' ')
    print(f'menuline([{", ".join(foods)}], [{", ".join(allergens)}]).')

