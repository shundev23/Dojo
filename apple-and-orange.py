#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # アルゴリズム
    # 1. りんごの位置を計算、配列:applePointに追加
    # 2. みかんの位置を計算、配列:orangePointに追加
    # 3. applePointの要素をfor文で取り出して、s <= applePoint[i] <= tの場合、カウントアップ
    # 4. orangePointの要素をfor文で取り出して、s <= orangePoint[i] <= tの場合、カウントアップ
    # 5. それぞれのカウントを出力

    applePoint = []
    orangePoint = []
    appleCount = 0
    orangeCount = 0

    for apple in apples:
        applePoint.append(a + apple)
    for orange in oranges:
        orangePoint.append(b + orange)
    
    for i in range(len(applePoint)):
        if s <= applePoint[i] <= t:
            appleCount += 1

    for j in range(len(orangePoint)):
        if s <= orangePoint[j] <= t:
            orangeCount += 1
    print(appleCount)
    print(orangeCount)

    # 内包表記で書くなら以下
    # appleCount = sum(s <= a + apple <= t for apple in apples)
    # orangeCount = sum(s <= a + orange <= t for apple in oranges)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
