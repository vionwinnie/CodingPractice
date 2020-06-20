#!/usr/bin/python3

import sys

test_num=int(sys.argv[1])

def harmonic_sum(num):

    print(num)

    if num <1:
        return 0
    else:
        if num ==1:
            return 1
        else:
            recip = 1/test_num
            return recip + harmonic_sum(num-1)


print(harmonic_sum(test_num))

