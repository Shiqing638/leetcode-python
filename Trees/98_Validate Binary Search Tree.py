class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = 0
        self.left = left
        self.right = right

import math

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, low=-math.inf, high=+math.inf):
            if not node:
                return True
            if node.val <= low or node.val>=high:
                return False

            return valid(node.left, low, node.val) and valid(node.right, node.val, high)
        return valid(root)