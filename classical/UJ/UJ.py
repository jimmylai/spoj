#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

while True:
    tokens = sys.stdin.readline().strip().split(" ")
    N, D = int(tokens[0]), int(tokens[1])
    if N == 0 and D == 0:
        break;
    print N**D

