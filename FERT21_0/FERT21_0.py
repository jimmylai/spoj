#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

num_lines = int(sys.stdin.readline())

for i in range(num_lines):
    N = float(sys.stdin.readline())
    answer = 1.0
    for i in range(int(N) - 1):
        answer /= N
    print answer
