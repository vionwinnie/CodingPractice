"""
Find longest consecutive consequence

   1 
   \
    2
    /\
   2  4
       \
        5
         \
          6

"""

class Node:
    def __init__(self,val=0):
        self.val = val
        self.left = None
        self.right= None

def searchLongestSequence(root):
    max_count = 1

    def searchSequence(parentNode,curNode):
        nonlocal max_count
        ## Case 1: Node is None
        if  curNode is None:
            return 1
        else:
            ## Root Node has no parent node
            if parentNode is None:
                cur_result = 0
            else:
                cur_result = compare(parentNode.val,curNode.val)
            left_result = searchSequence(curNode,curNode.left)
            right_result = searchSequence(curNode,curNode.right)
    
            ## if cur_result is 0 <- need to restart the count
            if cur_result==0:
                ## Update global variable max_count
                max_count = max(max_count,max(left_result,right_result))
                return 0
            else:
                return max(left_result,right_result)+1
    
    final = searchSequence(None,root)
    final_count = max(max_count,final)
    return final_count

def compare(prev_val,cur_val):
    if cur_val - prev_val ==1:
        return 1
    else:
        return 0



## Set up the example
def test_example_1():

    ## Set up Tree
    root = Node(1)
    root.right = Node(2)
    root.right.left = Node(3)
    root.right.left.right = Node(4)
    root.right.left.right.right = Node(8)
    root.right.left.right.right.right = Node(9)

    ## Run the example - Expect Answer = 4
    result = searchLongestSequence(root)
    assert result ==4

def test_example_2():

    ## Set up Tree
    root = Node(1)
    root.right = Node(2)
    root.right.left = Node(6)
    root.right.left.right = Node(7)
    root.right.left.right.right = Node(8)
    root.right.left.right.right.right = Node(9)

    result = searchLongestSequence(root)
    assert result ==4

def test_example_3():
    ## Set up Tree
    root = Node(1)
    result = searchLongestSequence(root)

    assert result ==1

