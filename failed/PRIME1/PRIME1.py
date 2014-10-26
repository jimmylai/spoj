#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

def generate_prime(N):
    for i in range(prime_list[-1], N, 2):
        if is_prime(i):
            prime_list.append(i)

def is_prime(N):
    half_N = int(N**0.5+1)
    if prime_list[-1] < half_N:
        generate_prime(half_N)

    for prime in [ i for i in prime_list if i <= half_N ]:
        if N % prime == 0:
            return False
    return True

def primes(n): 
    if n==2: return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
                i=i+1
                m=2*i+3
    return [2]+[x for x in s if x]

prime_list = [2,3,5,7]
num_lines = int(sys.stdin.readline())

for i in range(num_lines):
    tokens = sys.stdin.readline().split(" ")
    start, end = int(tokens[0]), int(tokens[1])
#    generate_prime(end)
    prime_list = primes(end)
    for prime in prime_list:
        if prime > end:
            break

        if prime >= start:
            print prime

    if i < num_lines-1:
        print ' '

