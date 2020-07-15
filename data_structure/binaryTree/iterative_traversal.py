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

## Post order - use two stacks
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 1. Push root to first stack.
        #2. Loop while first stack is not empty
            ## 2.1 Pop a node from first stack and push it to second stack
            ## 2.2 Push left and right children of the popped node to first stack
        # 3. Print contents of second stack


        stack1 = deque()
        stack2 = deque()

        cur_node = root
        stack1.append(cur_node)

        while stack1:
            cur_node = stack1.pop()
            stack2.append(cur_node)

            if cur_node.left:
                stack1.append(cur_node.left)
            if cur_node.right:
                stack1.append(cur_node.right)

        final_val = []
        while stack2:
            last_val = stack2.pop()
            final_val.append(last_val.val)

        return final_val

## TODO: Iterative In-order traversal
