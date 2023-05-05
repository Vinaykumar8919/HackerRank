# https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem?isFullScreen=true


#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum1=0
    a=1
    b=2
    c=2
    while c<n:
        if c%2==0:
            sum1+=c
        c=a+b
        a=b
        b=c
    print(sum1)
