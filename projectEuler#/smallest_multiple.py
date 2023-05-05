'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers 1 from N to ?


https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem?isFullScreen=true

'''


#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    number = n
    x=True
    while x:
        for i in range(1,n+1):
            if number%i!=0:
                number+=n
                break
        else:
            x=False
    print(number)
                
                
        
            
                
        
                
        