#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Module docstring
'''

__author__ = 'noahsark'

import sys

num = int(sys.stdin.readline().strip())

if num % 10 == 0:
    print 2
else:
    print 1
    print num % 10

