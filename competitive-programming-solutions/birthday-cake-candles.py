#!/bin/python3

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    # 1.candlesを降順にソート
    # 2.最大値を取り出す
    # 3.最大値を変数:max_valueに格納
    # 4.配列の残りの要素を取り出して、max_valueと一致したら、カウントアップする
    # 5.配列全部見終わった時点の、カウントを返す

    # max_value = sorted(candles, reverse=True)[0]
    # count = 1
    # for candle in sorted(candles, reverse=True)[0]:
    #     if candle == max_value:
    #         count += 1
    # return count

    max_value = max(candles)
    count = sum(1 for candle in candles if candle == max_value)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
