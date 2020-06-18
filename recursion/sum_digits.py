#!/usr/bin/python3

test_num = 1234554321
correct_answer = 30

def sum_digits(test_num):

    print(test_num)

    if test_num <10:
        return test_num

    else:
        ## Start with the last digit
        last_digit = test_num% 10
        remove_last_digit = (test_num-last_digit)/10
        rest_of_digit = sum_digits(remove_last_digit)

    return last_digit+rest_of_digit

my_answer = sum_digits(test_num)
assert correct_answer == my_answer
print("passed!~")

