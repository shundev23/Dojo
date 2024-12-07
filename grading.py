#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    # アルゴリズム
    # gradingを28未満かどうかで場合分け
    # 38未満 → そのままreturn
    # 38以上 → 成績とその次の5の倍数との差が3未満
    #         →５の倍数に繰り上げ
    # 　　　　　　　　　　　　　　　　　成績とその次の5の倍数との差が3以上は、成績を5の倍数に繰り上げる。
    #         → その他の場合は、そのままreturn
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            next_multiple_of_5 = (grade + 4) // 5 * 5
            if next_multiple_of_5 - grade < 3:
                result.append(next_multiple_of_5)
            else:
                result.append(grade)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
