"""
Leetcode #71 - Simplify Path

- Always begin with a slash
- Must be only a single slash
- must not end with training / 
- Canonical path = Shortest string representing the absolute path

"""

from collections import deque

def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    directories = [ s.strip() for s in path.split('/') if s.strip()]

    myStack = deque()
    i = 0

    while i < len(directories):
        cur_dir = directories[i]
        i+=1

        ## Go back up one level
        if cur_dir == '..':
            ## Pop if there is one level available
            if len(myStack) > 0:
                myStack.pop()

        elif cur_dir == '.':
            continue

        ## Add to stack for another level:
        else:
            myStack.append(cur_dir)


    ## Concatenate all elements:
    if len(myStack)>0:
        return '/'+'/'.join(myStack)
    else:
        return '/'


def test_answer():
    assert simplifyPath("/home/") == "/home"
    assert simplifyPath("/../") == "/"
    assert simplifyPath("/home//foo/") == "/home/foo"
    assert simplifyPath("/a/./b/../../c/") == "/c"
    assert simplifyPath("/a//b////c/d//././/..") == "/a/b/c"



