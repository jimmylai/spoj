#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Module docstring
'''

__author__ = 'noahsark'

import sys
from collections import Counter

s = sys.stdin.readline().strip()
c = Counter()
for i in s:
    c[i] += 1

result = []
curr = -1
buffer = []
for (char, count) in c.most_common(len(c)):
    if count != curr:
        result.extend(sorted(buffer))
        buffer = [char]
        curr = count
    else:
        buffer.append(char)

if len(buffer) > 0:
    result.extend(sorted(buffer))
print '\n'.join(result)
