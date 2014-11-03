#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Module docstring
'''

__author__ = 'noahsark'

import sys

num_test = int(sys.stdin.readline().strip())
for i in range(num_test):
    sys.stdin.readline()
    tokens = sys.stdin.readline().strip().split(' ')
    m, n = int(tokens[0]), int(tokens[1])
    ms = [int(sys.stdin.readline()) for _ in range(m - 1)]
    ns = [int(sys.stdin.readline()) for _ in range(n - 1)]
    ms.sort(reverse=True)
    ns.sort(reverse=True)
    cost = [0 for __ in range(n + 1) for _ in range(m + 1)]
    for x in range(1, m):
        print x * m, (x - 1) * m
        cost[x * m] = cost[(x - 1) * m] + ms[x - 1]
    for x in range(1, n):
        cost[x] = cost[x - 1] + ns[x - 1]
    for x in range(1, m):
        for y in range(1, n):
            cost[x * m + y] = min(cost[x * m + y - 1] + (x + 1) * ns[y - 1],
                                  cost[(x - 1) * m + y] + (y + 1) * ms[x - 1])
    print cost[(m - 1) * m + n - 1]
