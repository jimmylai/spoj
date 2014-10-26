#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

num_lines = int(sys.stdin.readline())

for i in range(num_lines):
    angess = [ int(i) for i in sys.stdin.readline().strip().split(" ") if i != "0" ]
    candidates = []
    while True:
        line = sys.stdin.readline().strip()
        if line == "0":
            break;
        candidates.append( [int(i) for i in line.split(" ") if i != "0"] )

    scores = []
    for candidate in candidates:
        score = [ [0 for j in range(len(candidate)+1) ]for i in range(len(angess)+1) ]
        for i, x in enumerate(angess):
            for j, y in enumerate(candidate):
                if x == y:
                    score[i+1][j+1] = score[i][j] + 1
                else:
                    score[i+1][j+1] = max(score[i][j+1], score[i+1][j])
        scores.append( score[len(angess)][len(candidate)])
    print max(scores)

