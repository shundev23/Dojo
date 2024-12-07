#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    n = len(arr)
    rations = [
        len(list(filter(lambda x: x > 0, arr))) / n,
        len(list(filter(lambda x: x < 0, arr))) / n,
        len(list(filter(lambda x: x == 0, arr))) / n
    ]

    for ration in rations:
        print(f"{ration:6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)