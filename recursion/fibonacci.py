#!/usr/bin/python3

import sys
import time

test_num = int(sys.argv[1])

def fibonacci_naive(num):
    if num ==0:
        return 0
    elif num ==1:
        return 1
    else:
        return fibonacci_naive(num-2)+fibonacci_naive(num-1)

fibonacci_dict = {0:0,1:1}

## Important lesson learnt:
## Using a Memo to Avoid Repetitious Calculation - memoization

def fibonacci_lookup(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        lookup = fibonacci_dict.get(num)
        ## new number, calculate
        if not lookup:
            result = fibonacci_lookup(num-2)+fibonacci_lookup(num-1)
            fibonacci_dict[num]=result
            return result
        else:
            return lookup

start_time = time.time()
print("Fibonacci number {} = {}".format(test_num,fibonacci_lookup(test_num)))

print("time taken for lookup: {:.2f}".format(time.time()-start_time))

start_time = time.time()
print("Fibonacci number {} = {}".format(test_num,fibonacci_naive(test_num)))
print("time taken for naive version: {:.2f}".format(time.time()-start_time))
