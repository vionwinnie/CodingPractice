#!/usr/bin/python3

test_num = 5
correct_answer = 5*4*3*2*1

def factorial(num):
    if num ==1:
        return 1
    else:
        return num*factorial(num-1)

my_answer = factorial(test_num)

assert correct_answer == my_answer
print("Passed!!")
