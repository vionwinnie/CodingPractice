# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


    def preorderTraversal(self, root: TreeNode) -> List[int]:

        vals = []

        if root:
            # Process Item
            vals.append(root.val)

            # First recur on left child
            vals.extend(self.preorderTraversal(root.left))

            # now recur on right child
            vals.extend(self.preorderTraversal(root.right))


        return vals


    def inorderTraversal(self, root: TreeNode) -> List[int]:

        vals = []

        if root:
            # First recur on left child
            vals = self.inorderTraversal(root.left)

            # Process Item
            vals.append(root.val)

            # now recur on right child
            vals.extend(self.inorderTraversal(root.right))

        return vals

    def postorderTraversal(self, root: TreeNode) -> List[int]:

        vals = []

        if root:
            # First recur on left child
            vals = self.postorderTraversal(root.left)

            # now recur on right child
            vals.extend(self.postorderTraversal(root.right))

            # Process Item
            vals.append(root.val)

        return vals


