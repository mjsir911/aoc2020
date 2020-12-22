#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

a = """
Player 1:
44
31
29
48
40
50
33
14
10
30
5
15
41
45
12
4
3
17
36
1
23
34
38
16
18

Player 2:
24
20
11
32
43
9
6
27
35
2
46
21
7
49
26
39
8
19
42
22
47
28
25
13
37
"""


a = a.strip().split('\n\n')

a = {b.split('\n')[0][:-1]: [int(c) for c in b.split('\n')[1:]] for b in a}


def round(b):
    # print("Player 1's deck: ", b['Player 1:'])
    # print("Player 2's deck: ", b['Player 2:'])
    draw = {p: c.pop(0) for p, c in b.items()}
    # print(f"Player 1 plays: {draw['Player 1:']}")
    # print(f"Player 2 plays: {draw['Player 2:']}")
    winner = max(draw, key=lambda p: draw[p])
    loser = 'Player 2' if winner == 'Player 1' else 'Player 1'
    b[winner].append(draw[winner])
    b[winner].append(draw[loser])
    # print(winner, 'wins the round!')
    # print()
    return b

print(a)
while all(a.values()):
    round(a)

from itertools import count
winner = a['Player 1'] or a['Player 2']
print(sum(c * d for c, d in zip(reversed(winner), count(start=1))))
