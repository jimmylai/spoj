#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys
from operator import itemgetter

__author__ = 'noahsark'

num_lines = int(sys.stdin.readline())

items = [ ( i+1, int(sys.stdin.readline()) ) for i in range(num_lines)]
items.sort(key=itemgetter(1))
total = sum([item[1] for item in items])
half = total / 2 + 1
load = 0

for item in items:
    if load + item[1] <= half:
        load += item[1]
        print item[0]
    else:
        break
