#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

num_lines = int(sys.stdin.readline().strip())

for i in range(num_lines):
    tokens = sys.stdin.readline().split(' ')
    rev_a, rev_b = int(tokens[0][::-1]), int(tokens[1][::-1])
    total = str(int(str(rev_a + rev_b)[::-1]))
    print total

