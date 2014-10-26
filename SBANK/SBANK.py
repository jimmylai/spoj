#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Program
'''

import sys


__author__ = 'noahsark'


def main():
    string = sys.stdin.readline().strip()
    t = int(string)
    final_output = ''

    for i in range(t):
        string = sys.stdin.readline().strip()
        n = int(string)
        count = {}
        for j in range(n):
            string = sys.stdin.readline().strip()
            if count.get(string) is None:
                count[string] = 1
            else:
                count[string] += 1

        if i > 0:
            final_output += '\n'
        keys = count.keys()
        keys.sort()
        for key in keys:
            final_output += key + ' ' + str(count[key]) + '\n'
        string = sys.stdin.readline().strip()
    sys.stdout.write(final_output)


main()
