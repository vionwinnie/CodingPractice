#!/usr/bin/python3

from collections import deque

## Using queues to check nested paranthesis
## Check answer using python -m pytest nested_paranthesis.py

def check_nested_parans(test_string):

    stack = deque()
    test_parans = list(test_string)
    
    if test_string[0]==')':
        return False
    else:
        for paran in test_parans:
            if paran=='(':
                stack.append(0)
            elif paran==')':
                if not stack:
                    return False
                    break
                else:
                    stack.pop()
            else:
                return False
                break
        print(stack)
        if not stack:
            return True
        else:
            return False

def test_answer():
    assert check_nested_parans('()()')==True
    assert check_nested_parans(')())')==False
    assert check_nested_parans('((()))()()(())')==True
    assert check_nested_parans('h())')==False
    assert check_nested_parans('())')==False
