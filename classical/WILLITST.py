#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Module docstring
'''

__author__ = 'noahsark'

import sys

n = int(sys.stdin.readline())
non_stops = set()
if n <= 1:
    print 'TAK'
else:
    first_time = set()
    first_time.add(n)
    while n > 1 and n not in non_stops:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 3

        if n in first_time:
            non_stops.add(n)
            break
        else:
            first_time.add(n)
    if n > 1:
        print 'NIE'
    else:
        print 'TAK'
