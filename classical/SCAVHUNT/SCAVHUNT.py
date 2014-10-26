#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

num_lines = int(sys.stdin.readline())

for i in range(1, num_lines+1):
    num_routes = int(sys.stdin.readline())
    routes = []
    for j in range(num_routes-1):
        tokens = sys.stdin.readline().strip().split(" ")
        routes.append( [tokens[0], tokens[1]] )
    while len(routes) > 1:
        start = routes[0][0]
        end = routes[0][-1]
        for route in routes:
            if end == route[0]:
                routes.append( routes.pop(0) + route[1:] )
                routes.remove( route )
                break
            if route[-1] == start:
                routes.append( route + routes.pop(0)[1:] )
                routes.remove( route )
                break

    if i > 1:
        print 
    print "Scenario #%d:" % i
    for route in routes[0]:
        print route

