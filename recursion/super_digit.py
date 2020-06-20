#!/usr/bin/python3

## Super Digit: 9875 -> 29 -> 11 -> 2 return 2

## Input 123,3 -> 123123123 

def sum_digit(num):

    if num <10:
        return num
    else:
        remainder = num%10
        next_num = (num-remainder)/10
        return sum_digit(next_num)+remainder

def check_num_length(num):
    while num > 10:
        print(num)
        new_num = sum_digit(num)
        num=new_num
    return num

n = 123
p = 6
## Pre-calculate such that it avoids numerical overflow
init_num = sum_digit(n)*6
print(init_num)
print(check_num_length(init_num))


