#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

num_lines = int(sys.stdin.readline())

for i in xrange(num_lines):
    N = int(sys.stdin.readline())
    piles = [ [idx+1, int(j)] for idx, j in enumerate(sys.stdin.readline().strip().split(" ")) ]
    for idx, pile in enumerate(piles):
        if pile[1] < pile[0]:
            piles.pop(idx)
    count = 0
    while len(piles) > 0:
        for idx, pile in enumerate(piles):
            if pile[1] >= pile[0]:
                count += 1
                pile[1] -= pile[0]
            else:
                piles.pop(idx)
                break

    if count % 2 == 1:
        print "ALICE"
    else:
        print "BOB"

