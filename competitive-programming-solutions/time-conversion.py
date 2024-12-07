#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

def timeConversion(s):
    try:
        time_obj = datetime.strptime(s, "%I:%M:%S%p")
        return time_obj.strftime("%H:%M:%S")
    except ValueError as e:
        return f"Invalid time format: {e}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
