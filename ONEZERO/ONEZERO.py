#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys
import re

__author__ = 'noahsark'

num_lines = int(sys.stdin.readline())

for i in range(num_lines):
    N = int(sys.stdin.readline())
    answer, num = N, 2
    while True:
        string = str(answer)
        if len(re.findall(r"""[23456789]""", string)) == 0:
            print answer
            break
        else:
            answer = N * num
            num += 1

