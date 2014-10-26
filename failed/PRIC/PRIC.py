#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys

__author__ = 'noahsark'

prime_list = [2,3,5,7]

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

const = 2**31
a = 1

def f(a):
    return (a+1234567890) % const

sys.stdout.write('0')
count = 1
while True:
    if count > 51:
        break
    a = f(a)
    if is_prime( a ):
        sys.stdout.write('1')
    else:
        sys.stdout.write('0')
    count += 1

