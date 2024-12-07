#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    n = len(arr)
    prinmary_sum = 0
    secondary_sum = 0
    
    for i in range(n):
        prinmary_sum += arr[i][i]
        secondary_sum += arr[i][n-i-1]
    return abs(prinmary_sum - secondary_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
