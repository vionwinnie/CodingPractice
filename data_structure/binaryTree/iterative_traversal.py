# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
def preorderTraversal(self,root:TreeNode) -> List[int]:

    stack = deque()
    all_num = []

    ## Process Item
    cur_node = root
    stack.append(cur_node)

    while stack:
        my_node = stack.pop()
        if my_node:
            stack.append(my_node.right)
            stack.append(my_node.left)
            all_num.append(my_node.val)

    return all_num


