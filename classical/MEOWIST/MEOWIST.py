#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys
import operator

__author__ = 'noahsark'

friends = []
while True:
    string = sys.stdin.readline()
    if string == "":
        break;
    name, age = string.split(" ")[0], int(string.split(" ")[1])
    friends.append( (name, age) )
friends.sort(key = operator.itemgetter(0))
friends.sort(key = operator.itemgetter(1), reverse=True)
for name, age in friends:
    print name
