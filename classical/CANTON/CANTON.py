#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

num_lines = int(sys.stdin.readline())

for i in range(num_lines):
    N = int(sys.stdin.readline())
    n = 1
    count = 0
    while count+n < N:
        count += n
        n += 1
    if n % 2 == 0:
        up = N - count
        down = n+1-up
    else:
        up = n - (N - count) + 1
        down = n+1-up

    print "TERM %d IS %d/%d" % (N, up, down)

