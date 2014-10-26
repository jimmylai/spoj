#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

def cal_score(a, b):
    if a == b:
        return 1
    elif a == 'S':
        if b == 'P':
            return 2
    elif a == 'P':
        if b == 'R':
            return 2
    elif a == 'R':
        if b == 'S':
            return 2
    return 0

num_rounds = int(sys.stdin.readline())
sven = sys.stdin.readline().strip()
num_friends = int(sys.stdin.readline())
friends = {}
for i in range(num_friends):
    friends[i] = sys.stdin.readline().strip()

score_sven = 0
for seq in friends.values():
    for i, symbol in enumerate(sven):
        score_sven += cal_score(symbol, seq[i])

print score_sven

score_max = 0
for i in range(num_rounds):
    score_max += max( [sum([ cal_score('S', seq[i]) for seq in friends.values() ]),
                        sum([ cal_score('P', seq[i]) for seq in friends.values() ]),
                        sum([ cal_score('R', seq[i]) for seq in friends.values() ])] )
print score_max

