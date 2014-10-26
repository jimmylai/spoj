#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

tokens = sys.stdin.readline().split(" ")
num_lines = int(tokens[0])
k = int(tokens[1])
total = 0

lines = sys.stdin.read().split('\n')
for i, line in enumerate(lines):
    if i > num_lines-1:
        break
    N = int(line)
    if N % k == 0:
        total += 1
print total
