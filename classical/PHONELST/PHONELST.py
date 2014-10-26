#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

num_lines = int(sys.stdin.readline())

for i in range(num_lines):
    n = int(sys.stdin.readline())
    l = []
    for j in range(n):
        l.append(sys.stdin.readline().strip())
    l.sort()
    is_consistant = True
    for j in range(0, n-1):
        if l[j+1].startswith(l[j]):
            is_consistant = False
            break
    if is_consistant:
        print "YES"
    else:
        print "NO"

