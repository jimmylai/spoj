#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

for line in sys.stdin:
    num = int(line)
    if num != 42:
        print num
    else:
        break

