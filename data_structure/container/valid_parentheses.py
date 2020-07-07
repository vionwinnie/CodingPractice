"""
Leetcode #20 - Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

"""

from collections import deque
check_dict = { '(':1, '{':2, '[':3 ,')':-1,'}':-2,']':-3}

def decode(s):
    return check_dict.get(s,0)      
               
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """       

    ## Initialize stack and counter
    myStack = deque()
    result = True  ## for empty string, return true
    i = 0
        
    ## Going through the string 
    while i < len(s):
        cur = s[i]
        num = decode(cur)
         
        i +=1
        ## If open paran -> add to stack
        if num >0:
            myStack.append(num)

        ## If closing paran -> pop the stack
        else:
            try:
                last = myStack.pop()
                neutral = num + last
                ## If any of them do not match, then return False
                if neutral != 0:
                    result = False
                    break
            except:
                result = False
     
    if len(myStack)>0:
        result = False
    
    return result


def test_answer():
    assert isValid('()') == True
    assert isValid('') == True
    assert isValid('()[]{}')== True
    assert isValid('(]')==False
    assert isValid('(')==False
    assert isValid('{[]}')==True
