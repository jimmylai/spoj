#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

num_lines = int(sys.stdin.readline())

def tokenize(string):
    l = [0]
    prev = string[0].isdigit()
    for i in range(1, len(string)):
        if string[i].isdigit() != prev:
            l.append(i)
            prev = string[i].isdigit()

    rst = []
    for i in range(1, len(l)):
        rst.append( string[l[i-1]:l[i]].strip() )

    rst.append( string[l[-1]:].strip() )
    return rst

for i in range(num_lines):
    sys.stdin.readline()
    tokens = tokenize( sys.stdin.readline().strip() )
    result = tokens[0]
    for i in range(1, len(tokens), 2):
        if tokens[i] == "=":
            break;
        result += tokens[i] + tokens[i+1]
        result = str( eval(result) )
    print result

