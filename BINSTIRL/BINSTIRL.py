#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

def stiring_number(n, m):
    if n == 0 and m == 0:
        return 1
    if m == 0:
        return 0
    if n == 0:
        return 0
    return m*stiring_number(n-1, m) + stiring_number(n-1, m-1)

num_lines = int(sys.stdin.readline())

for i in range(num_lines):
    tokens = sys.stdin.readline().strip().split(" ")
    n, m = int(tokens[0]), int(tokens[1])
    print stiring_number(n, m) % 2

