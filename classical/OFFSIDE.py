#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Module docstring
'''

__author__ = 'noahsark'

import sys

while True:
    tokens = sys.stdin.readline().strip().split()
    A, D = int(tokens[0]), int(tokens[1])
    if A == 0 and D == 0:
        break

    attachs = [int(i) for i in sys.stdin.readline().strip().split(' ')]
    defenses = [int(i) for i in sys.stdin.readline().strip().split(' ')]

    attachs.sort()
    defenses.sort()

    result = 'N'
    if len(attachs) > 0:
        if len(defenses) > 0:
            if attachs[0] < defenses[0]:
                result = 'Y'
            if len(defenses) >= 2:
                if attachs[0] < defenses[1]:
                    result = 'Y'
    print result

