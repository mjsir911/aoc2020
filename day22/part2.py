#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

from sys import stdin
a = stdin.read().strip().split('\n\n')


# class list(list): pass

a = {b.split('\n')[0][:-1]: list(int(c) for c in b.split('\n')[1:]) for b in a}


def draw(b):
    return {p: c.pop(0) for p, c in b.items()}


def fight(b):
    # print('-- Round --')
    # print(b)
    d = draw(b)
    if len(b['Player 1']) >= d['Player 1'] and len(b['Player 2']) >= d['Player 2']:
        winner = game({
            'Player 1': list(b['Player 1'][:d['Player 1']]),
            'Player 2': list(b['Player 2'][:d['Player 2']]),
        })
        # winner = game(deepcopy(b))
    else:
        winner = 'Player 1' if d['Player 1'] > d['Player 2'] else 'Player 2'
    # print(f'winner: {winner}')
    # winner = max(draw, key=lambda p: draw[p])
    loser = 'Player 2' if winner == 'Player 1' else 'Player 1'
    b[winner].append(d[winner])
    b[winner].append(d[loser])
    # print(winner, 'wins the round!')
    # print()


def game_to_hashable(b):
    return (tuple(b['Player 1']), tuple(b['Player 2']))


def game(b):
    seen = set()
    # print('=== Game ===')
    while b['Player 1'] and b['Player 2']:
        c = game_to_hashable(b)
        if c in seen:
            return 'Player 1'
        seen.add(c)
        fight(b)

    winner = 'Player 1' if b['Player 1'] else 'Player 2'
    return winner

from itertools import count
# winner = a['Player 1'] or a['Player 2']
winner = a[game(a)]
print(a)
print(sum(c * d for c, d in zip(reversed(winner), count(start=1))))
