#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Module docstring
'''

__author__ = 'noahsark'

import sys

cache = {}
def x(n, a, b, m, x1):
    if n == 1:
        return x1
    if n in cache:
        return cache[n]
    cache[n] = (a * x(n-1, a, b, m, x1) + b) % m
    return cache[n]

line = sys.stdin.readline()
tokens = line.split(' ')
a, b, x1, k, m = int(tokens[0]), int(tokens[1]), int(tokens[2]), int(tokens[3]), int(tokens[4])
for i in range(1, k):
    x(i, a, b, m, x1)

for i in range(k, k+5):
    print x(i, a, b, m, x1)
