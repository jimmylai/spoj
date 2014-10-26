#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Program
'''

import sys
import math


__author__ = 'noahsark'


t = int(sys.stdin.readline().strip())
output = ''
for i in xrange(t):
    n = int(sys.stdin.readline().strip())
    answer = 0
    for j in xrange(1, int(math.sqrt(n)) + 1):
        if n % j == 0:
            num = n / j
            if num == j:
                answer += num
            else:
                answer += j
                if num < n:
                    answer += num
    output += '%d\n' % (answer)

print output
