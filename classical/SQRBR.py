#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Module docstring
'''

__author__ = 'noahsark'

import sys

n = 0
arr = []
dp = [[]]


def solve(pos, open):
    if open < 0:
        return 0
    if pos == n:
        if open == 0:
            return 1
        else:
            return 0
    if dp[pos][open] != -1:
        return dp[pos][open]
    if arr[pos] is True:
        dp[pos][open] = solve(pos + 1, open + 1)
        return dp[pos][open]
    dp[pos][open] = solve(pos + 1, open - 1) + solve(pos + 1, open + 1)
    return dp[pos][open]


d = int(sys.stdin.readline())
for i in range(d):
    tokens = sys.stdin.readline().strip().split(' ')
    n, k = int(tokens[0]) * 2, int(tokens[1])
    arr = [False for z in range(n)]
    dp = [[-1 for x in range(n)] for y in range(n)]
    for tok in sys.stdin.readline().split(' '):
        arr[int(tok) - 1] = True
    print solve(0, 0)
