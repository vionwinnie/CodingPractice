#!/usr/bin/python3

test_data = [1, 2, [3,4], [5,[1,2,3]]]
correct_answer = 21


## Breaking down into smaller problem.....
## Mission statement: sum if every element is int, else recurse

def list_sum(list_num):
    print(list_num)
    check = all(isinstance(x, int) for x in list_num)

    if check:
        print(sum(list_num))
        return sum(list_num)
    else:
        ## Break it into smaller problem
        tmp = [x for x in list_num if isinstance(x,int)]
        int_in_list_sum = sum(tmp)
        smaller_problems = [x for x in list_num if not isinstance(x,int)]
        ## LIST IS NOT CALLABLE IN RECURSION
        solved_small_problems = [list_sum(small) for small in smaller_problems]
        sum_all_probs = sum(solved_small_problems)
        return int_in_list_sum + sum_all_probs

my_answer = list_sum(test_data)
assert my_answer== correct_answer
print("Passed~!")
