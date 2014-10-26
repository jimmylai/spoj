#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

num_lines = int(sys.stdin.readline())

for i in range(num_lines):
    N = int(sys.stdin.readline())
    total = 1
    for i in range(2, N+1):
        total *= i
    print total

