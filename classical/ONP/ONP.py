#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Program
'''

import sys


__author__ = 'noahsark'


while True:
    string = sys.stdin.readline().strip()
    if string == '':
        break

    N = int(string)
    for i in range(N):
        string = sys.stdin.readline().strip()
        operators = ['+', '-', '*', '/', '^']
        operands = []
        stack = []
        output = ''
        for c in string:
            if c == '(':
                continue
            elif c == ')':
                output += stack.pop()
            elif ord(c) >= ord('a') and ord(c) <= ord('z'):
                output += c
            elif c in operators:
                stack.append(c)
        while len(stack) > 0:
            output += stack.pop()
        print output
