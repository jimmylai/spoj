#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Module docstring
'''

__author__ = 'noahsark'

import sys

def is_lucky(n):
    count = 0
    p = 2
    while n > 1:
        while n % p != 0:
            p += 1
        count += 1
        if count == 3:
            return True
        while n % p == 0:
            n /= p
    return False

arr = [i for i in range(1, 1001) if is_lucky(i)]
is_lucky(30)
t = int(sys.stdin.readline())
count = 0
while count < t:
    input = sys.stdin.readline().strip()
    if len(input) == 0:
        print
        continue
    n = int(input)
    print arr[n-1]
