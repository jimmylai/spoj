#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Module docstring
'''

__author__ = 'noahsark'

import sys

primes = [2, 3, 5, 7, 11]
for i in range(13, 10000, 2):
    is_prime = True
    for prime in primes:
        if i % prime == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

primes = [str(i) for i in primes if i >= 1000]


def is_connect(a, b):
    num_diff = len([1 for (i, j) in zip(a, b) if i != j])
    if num_diff == 1:
        return True
    return False


graph = {}
for i in primes:
    for j in primes:
        if is_connect(i, j):
            if i not in graph:
                graph[i] = []
            graph[i].append(j)


def shortest_path(a, b):
    cur = [a]
    for i in range(len(primes)):
        if b in cur:
            return i
        cur = set([k for j in cur for k in graph.get(j, [])])
    return 'Impossible'


num = int(sys.stdin.readline())
for i in range(num):
    tokens = sys.stdin.readline().strip().split(' ')
    start, end = tokens[0], tokens[1]
    print shortest_path(start, end)
