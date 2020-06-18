#!/usr/bin/python3

import os
print("Hello World!")

list_num = [2,3,4,5,5,222,123]

def add_sum(list_num):
    print(list_num)
    if len(list_num)== 1:
        return list_num[0]
  
    else:
        left_idx = int(len(list_num)/2)
        left_list = list_num[:left_idx]
        right_list = list_num[left_idx:]
    
    return add_sum(left_list)+add_sum(right_list)

correct_answer=sum(list_num)
my_answer = add_sum(list_num)

print("Correct Answer:{}".format(correct_answer))
print("My Answer:{}".format(my_answer))
assert my_answer==correct_answer
print("Passed~!!")



