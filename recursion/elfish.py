#!/usr/bin/python3

import sys

input_str = sys.argv[1]
pattern = sys.argv[2]
test_string='waffles'
test_pattern='elf'

## Mission: look up all the words in the pattern

# Break when all characters are found
# Break when finishes search

def elfish(test_string,pattern,count):
    print("test_string:{}".format(test_string))
    print("pattern:{}".format(pattern))
    print("count:{}".format(count))

    if len(test_string)==0:
        return False
    elif count ==3:
        return True
    else:
        character_to_check = test_string[0]
        pattern_list = list(pattern)
        if character_to_check in list(pattern):
            count +=1
            pattern_list.remove(character_to_check)
            new_pattern = ''.join(pattern_list)
            return elfish(test_string[1:],new_pattern,count)
        else:
            return elfish(test_string[1:],pattern,count)
            
            new_pattern = pattern.drop(character)

print(elfish(test_string,test_pattern,0))


def x_init(test_string,pattern):

    ## find set of pattern
    unique_pattern = "".join(list(set(list(pattern))))
    count = len(unique_pattern)

    return x_ish(test_string,unique_pattern,0,count)


def x_ish(test_string,pattern,count,length):
    print("test_string:{}".format(test_string))
    print("pattern:{}".format(pattern))
    print("count:{}".format(count))

    if len(test_string)==0:
        return False
    elif count ==length:
        return True
    else:
        character_to_check = test_string[0]
        pattern_list = list(pattern)
        if character_to_check in list(pattern):
            count +=1
            pattern_list.remove(character_to_check)
            new_pattern = ''.join(pattern_list)
            return x_ish(test_string[1:],new_pattern,count,length)
        else:
            return x_ish(test_string[1:],pattern,count,length)

print(x_init(input_str,pattern))
