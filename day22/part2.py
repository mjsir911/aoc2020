#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

from sys import stdin
a = stdin.read().strip().split('\n\n')


# class list(list): pass

a = tuple(list(int(c) for c in b.split('\n')[1:]) for b in a)


def draw(b):
    return b[0].pop(0), b[1].pop(0)


def fight(b):
    # print('-- Round --')
    # print(b)
    d = draw(b)
    if len(b[0]) >= d[0] and len(b[1]) >= d[1]:
        winner = game((
            list(b[0][:d[0]]),
            list(b[1][:d[1]]),
        ))
        # winner = game(deepcopy(b))
    else:
        winner = 0 if d[0] > d[1] else 1
    # print(f'winner: {winner}')
    # winner = max(draw, key=lambda p: draw[p])
    loser = 1 if winner == 0 else 0
    b[winner].append(d[winner])
    b[winner].append(d[loser])
    # print(winner, 'wins the round!')
    # print()


def game_to_hashable(b):
    return (tuple(b[0]), tuple(b[1]))


def game(b):
    seen = set()
    # print('=== Game ===')
    while b[0] and b[1]:
        c = game_to_hashable(b)
        if c in seen:
            return 0
        seen.add(c)
        fight(b)

    winner = 0 if b[0] else 1
    return winner

from itertools import count
winner = a[game(a)]
print(a)
print(sum(c * d for c, d in zip(reversed(winner), count(start=1))))
