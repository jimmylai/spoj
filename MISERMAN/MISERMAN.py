#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'


string = sys.stdin.readline().strip()

N, M = int(string.split()[0]), int(string.split()[1])
flares = []
for i in range(N):
    arr = [int(i) for i in sys.stdin.readline().strip().split()]
    flares.append(arr)

costs = [flares[0]]
for i in range(1, N):
    arr = []
    for j in range(0, M):
        cost = sys.maxint
        cost = min(cost, costs[i - 1][j] + flares[i][j])
        if j - 1 >= 0:
            cost = min(cost, costs[i - 1][j - 1] + flares[i][j])
        if j + 1 < M:
            cost = min(cost, costs[i - 1][j + 1] + flares[i][j])
        arr.append(cost)
    costs.append(arr)

print min(costs[-1])
