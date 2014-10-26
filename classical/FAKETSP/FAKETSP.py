#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys
import re

__author__ = 'noahsark'

total = float(0)
prev_x, prev_y = None, None
while True:
    string = sys.stdin.readline()
    if string == "":
        break

    rst = re.findall(r"""\((.+), (.+)\)""", string)[0]
    x, y = float(rst[0]), float(rst[1])
    if prev_x != None:
        total += ( (x - prev_x)**2 + (y - prev_y)**2 )**0.5
        print "The salesman has traveled a total of %.3f kilometers." % total
    prev_x, prev_y = x,y

