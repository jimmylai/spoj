#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys
import re

__author__ = 'noahsark'

def print_run_length(c, count):
    if count <= 9:
        sys.stdout.write( str(count) )
        sys.stdout.write(c)
    else:
        sys.stdout.write( "9" )
        sys.stdout.write(c)
        print_run_length(c, count-9)


while True:
    string = sys.stdin.readline().strip()
    if string == "":
        break;
    sys.stdout.write(string + " = ")
    tokens = string.split(" ")
    cmd = str()
    for token in tokens:
        if token.isdigit():
            num = str()
            for i in range(0, len(token), 2):
                num += token[i+1] * int(token[i])
            cmd += " " + num
        else:
            cmd += " " + token
    answer = str(eval(cmd))

    prev = answer[0]
    count = 1
    for c in answer[1:]:
        if c == prev:
            count += 1
        else:
            print_run_length(prev, count)
            count = 1
            prev = c
    print_run_length(prev, count)
    sys.stdout.write('\n')
