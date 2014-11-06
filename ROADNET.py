#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Module docstring
'''

__author__ = 'noahsark'

import sys

t = int(sys.stdin.readline())
for idx in range(t):
    if idx > 0:
        _ = sys.stdin.readline()
        print
    n = int(sys.stdin.readline())
    net = []
    nbr = [[[] for i in range(n)] for j in range(n)]
    for __ in range(n):
        tokens = sys.stdin.readline().strip().split(' ')
        net.append([int(i) for i in tokens])
    for row in net:
        for i in range(n):
            if row[i] == 0:
                row[i] = sys.maxint
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if net[i][k] == sys.maxint or net[k][j] == sys.maxint:
                    continue
                if net[i][k] + net[k][j] <= net[i][j]:
                    net[i][j] = net[i][k] + net[k][j]
                    nbr[i][j].append(k)
    for i in range(n):
        for j in range(i + 1, n):
            if len(nbr[i][j]) == 0:
                print i + 1, j + 1
