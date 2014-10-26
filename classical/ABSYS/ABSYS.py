#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

num_lines = int(sys.stdin.readline())

def check_number(s):
    if s.isdigit():
        return int(s)
    else:
        return None

for i in range(num_lines):
    sys.stdin.readline()
    tokens = sys.stdin.readline().strip().split(" ")
    # a + b = c
    a = check_number(tokens[0])
    b = check_number(tokens[2])
    c = check_number(tokens[4])

    if a == None:
        a = c - b

    if b == None:
        b = c - a

    if c == None:
        c = a + b

    print '%d +  %d = %d' % (a, b, c)

