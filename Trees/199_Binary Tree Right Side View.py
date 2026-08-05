# Methode 1: BFS
# Methode 2: DFS
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
# class Solution:
#     def rightSideView(self, root: TreeNode) -> list[int]:
#         res = []

#         q = deque()
#         q.append(root)

#         while q:
#             cur_length = len(q)
#             for _ in range(cur_length):
#                 cur = q.popleft()
#                 if not cur:
#                     return []
#                 if cur.left:
#                     q.append(cur.left)
#                 if cur.right:
#                     q.append(cur.right)
#             res.append(cur.val)
#         return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        res = []
        def dfs(node, depth):
            if not node:
                return 
            if depth == len(res):
                res.append(node.val)
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)

        dfs(root, 0)
        return res
