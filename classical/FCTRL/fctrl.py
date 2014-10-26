#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

num_lines = int(sys.stdin.readline().strip())

for i in range(num_lines):
    N = int(sys.stdin.readline().strip())
    total = 0
    while N/5 > 0:
        N = N/5
        total += N
    print total
