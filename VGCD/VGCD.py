#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

num_lines = int(sys.stdin.readline())

for i in range(num_lines):
    m = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    mm = m
    nn = n
    if m < n:
        m, n = n, m
    while m % n != 0:
        t = m % n
        m = n
        n = t
    print n

