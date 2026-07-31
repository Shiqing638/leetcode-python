class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque
class Solution:
    def nnn(self, root: Optional[TreeNode]):
        q = deque()
        q.append(root)
        res = []
        

        while q:
            cur = []
            for _ in range(len(q)):
                node = q.popleft()

                cur.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(cur)
        return res