# Methode 1: inorder dfs
# Methode 2: stack

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1:
# class Solution:
#     def kkk(self, root: TreeNode, k: int) -> int:
#         res = []
#         def inorder(node):
#             if not node:
#                 return 
#             inorder(node.left)
#             res.append(node.val)
#             inorder(node.right)

#         inorder(root)
#         return result[k-1]

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right