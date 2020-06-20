#!/usr/bin/python3

import sys

test_num = int(sys.argv[1])

def sum_other(num):
    print(num)
    if num <=0:
        return 0
    else:
        return num+sum_other(num-2)

print(sum_other(test_num))
