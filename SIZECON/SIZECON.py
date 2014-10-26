#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

num_lines = int(sys.stdin.readline().strip())
total = 0

for i in range(num_lines):
    N = int(sys.stdin.readline().strip())
    if N > 0:
        total += N
print total

