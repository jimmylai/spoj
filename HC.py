#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Module docstring
'''

__author__ = 'noahsark'

import sys

num_tests = int(sys.stdin.readline())

for i in range(num_tests):
    num_lines = int(sys.stdin.readline())
    rlt = False
    for j in range(num_lines):
        name = sys.stdin.readline().strip()
        if name == 'lxh':
            rlt = rlt != True
        else:
            rlt = rlt != False
    if rlt is True:
        print 'lxh'
    else:
        print 'hhb'
