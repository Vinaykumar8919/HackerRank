#  https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem?isFullScreen=true
#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    multiplesof3 = (n-1)//3
    multiplesof5= (n-1)//5
    multiplesof15 = (n-1)//15
    sum3=int(3*multiplesof3*(multiplesof3+1)//2)
    sum5=int(5*multiplesof5*(multiplesof5+1)//2)
    sum15=int(15*multiplesof15*(multiplesof15+1)//2)
    sum=sum3+sum5-sum15
    print(int(sum))
