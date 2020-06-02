#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    lst=[0]*(n+1)
    lst[0]=1
    i=1
    while(n>0):
        if i%2==0:
            lst[i]=lst[i-1]+1
            i=i+1
        else:
            lst[i]=lst[i-1]*2
            i=i+1
        n=n-1    
    return max(lst)       
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
