#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

while True:
    string = sys.stdin.readline()
    if string == "":
        break

    total = int(string)
    num_added = int(sys.stdin.readline())
    num_lower = (total - num_added) / 2
    print num_lower + num_added
    print num_lower

