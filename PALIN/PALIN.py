#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Program
'''

import sys


__author__ = 'noahsark'


def plus_one(string):
    for i, char in enumerate(string):
        if char == '9':
            string[i] = '0'
            if i == len(string) - 1:
                string.append('1')
                return string
            else:
                return string[:i + 1] + plus_one(string[i + 1:])
        else:
            string[i] = chr(ord(char) + 1)
            return string


def check_palin(string):
    for i, j in zip(string, string[::-1]):
        if i != j:
            return False
    return True

t = int(sys.stdin.readline().strip())
output = ''
for i in xrange(t):
    string = sys.stdin.readline().strip()
    string = list(string[::-1])
    while True:
        string = plus_one(string)
        if check_palin(string) is True:
            string.reverse()
            output += ''.join(string) + '\n'
            break
print output
