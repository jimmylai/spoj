#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

num_lines = int(sys.stdin.readline())

for i in range(num_lines):
    sys.stdin.readline()
    length = int(sys.stdin.readline())
    seq = sys.stdin.readline().strip().split(" ")
    seq = [ int(i) for i in seq ]
    start, end = 0, 1
    count = 0
    while start < len(seq) and end <= len(seq) :
        if sum(seq[start:end]) < 47:
            end += 1
        elif sum(seq[start:end]) > 47:
            start += 1
        else:
            count += 1
            start += 1
            end += 1
    print count

