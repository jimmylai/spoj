#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Module docstring
'''

__author__ = 'noahsark'

import sys

t = int(sys.stdin.readline())
for i in range(t):
    tokens = sys.stdin.readline().strip().split(' ')
    N, order = tokens[0], int(tokens[1])
    if order == 0:
        print 'Airborne wins.'
    elif order == 1:
        print 'Pagfloyd wins.'
