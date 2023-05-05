# problem link
# https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem?isFullScreen=true


#!/bin/python3

import sys

def product1(li):
    product =1 
    for i in li:
        product*=int(i)
    return product
t = int(input().strip())

for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    N=num = input().strip()
    # -------------------method 1 --------------
    li = list(num)
    maxProduct=0
    for i in range(k,len(li)):
        temp=int(product1(li[i-k:i]))
        
        if maxProduct<temp:
            maxProduct=temp
    print(maxProduct)
    
    # --------------------------method 2-----------
    # i = 0
    # mx = 0
    # while True:
    #     s = N[i : i + k]
    #     if len(s) < k: break
    #     if "0" in s:
    #         i += s.find("0") + 1
    #     else:
    #         mul = 1
    #         for l in s: mul *= int(l) 
    #         if  mul > mx: 
    #             mx = mul
    #         i += 1
    # print(mx)

