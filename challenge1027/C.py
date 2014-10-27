#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Module docstring
'''

__author__ = 'noahsark'

import sys

tokens = sys.stdin.readline().split(' ')
N, Q = int(tokens[0]), int(tokens[1])
net = [[-1 for i in range(N)] for j in range(N)]

def check(a, b, limit):
    cost = [[False for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if net[i][j] != -1 and limit <= net[i][j]:
                cost[i][j] = True
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if k == i or k == j or cost[i][j] is True:
                    continue
                if limit <= net[i][k] and limit <= net[k][j]:
                    cost[i][j] = True
                if cost[i][k] == True and cost[k][j] == True:
                    cost[i][j] = True

    return cost[a][b]


for i in range(Q):
    tokens = sys.stdin.readline().strip().split(' ')
    inc, a, b, limit = tokens[0], int(tokens[1])-1, int(tokens[2])-1, int(tokens[3])
    if inc == 'make':
        if net[a][b] == -1:
            net[a][b] = limit
            net[b][a] = limit
        elif net[a][b] <= limit:
            net[a][b] = limit
            net[b][a] = limit

    elif inc == 'check':
        if check(a, b, limit) is True:
            print 'YES'
        else:
            print 'NO'
