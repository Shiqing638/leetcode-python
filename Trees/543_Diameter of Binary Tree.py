class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sss(self, root: TreeNode) -> int:
        res = 0
        def dfs(node):
            if not node:
                return 0
            length = dfs(node.left) + dfs(node.right)
            res = max(res, length)

        return dfs(0)

