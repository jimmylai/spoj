#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Module docstring
'''

__author__ = 'noahsark'

import sys
import copy

N = int(sys.stdin.readline())
arr = [[False for i in range(N)] for j in range(N)]
for row in range(N):
    line = sys.stdin.readline().strip()
    for col, c in enumerate(line):
        if c == 'Y':
           arr[row][col] = True


count = 0.0
conn = [[[-1 for i in range(N)] for j in range(N)] for k in range(N)]
prob = [0.0 for i in range(N)]
prob[0] = 1.0
score = 1.0

for k in range(1, N):
    for i in range(N):
        wait = []
        for j in range(N):
            if arr[i][j] is True and prob[i] != 0.0 and prob[j] == 0.0:
                wait.append(j)
        for x in wait:
            prob[x] = prob[i] / float(len(wait))
            score += prob[x] * k

print prob
print score
