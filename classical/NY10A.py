#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Module docstring
'''

__author__ = 'noahsark'

import sys

patterns = {'TTT': 0, 'TTH': 1, 'THT': 2, 'THH': 3, 'HTT': 4, 'HTH': 5, 'HHT': 6, 'HHH': 7}

N = int(sys.stdin.readline())
for i in range(N):
    num = sys.stdin.readline().strip()
    seq = sys.stdin.readline().strip()
    counts = [0 for j in range(len(patterns))]
    for j in range(0, len(seq) - 2):
        counts[patterns[seq[j:j + 3]]] += 1
    print '%s %s' % (num, ' '.join(map(str, counts)))
