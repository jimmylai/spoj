#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys
import math

__author__ = 'noahsark'

pi = 2*math.acos(0)
while True:
    l = float(sys.stdin.readline())
    if l == 0:
        break;

    r = l/pi
    print '%.2f' % ( pi * r * r / 2.0 )

