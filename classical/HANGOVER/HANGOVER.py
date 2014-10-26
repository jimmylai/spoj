#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

while True:
    N = float( sys.stdin.readline() )
    if N == 0.0:
        break
    count, total = 2.0, 0.0
    while total < N:
        total += 1.0/count
        count += 1.0
    print "%d card(s)" % ( int(count-2) )

