#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'


while True:
    string = sys.stdin.readline().strip()
    if string == ".":
        break
    text, times = string.split(" ")[0], int(string.split(" ")[1])
    string = text * times
    for i in range( len(text) ):
        print string
        string = string[1:] + string[0]

