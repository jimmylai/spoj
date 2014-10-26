#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

num_column = int(sys.stdin.readline())
while num_column != 0:
    string = sys.stdin.readline().strip()
    result = str()
    for j in range(0, num_column):
        result += string[j]
        for i in range(2*num_column, len(string) + 2*num_column, 2*num_column):
            if i-1-j < len(string):
                result += string[i-1-j]
            if i+j < len(string):
                result += string[i+j]
    print result
    num_column = int(sys.stdin.readline())



