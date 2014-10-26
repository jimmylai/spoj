#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

def f(n, a, b):
    if n == 0:
        return 1
    else:
        return a*f(n-1, a, b) + b

num_lines = int(sys.stdin.readline())

for i in range(num_lines):
    tokens = sys.stdin.readline().strip().split(" ")
    a = int(tokens[0])
    b = int(tokens[1])
    n = int(tokens[2])
    M = int(tokens[3])
    print f(n, a, b) % M

