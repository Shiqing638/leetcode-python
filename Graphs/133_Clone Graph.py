class Node:
    def __init__(self, val=0, neighbors = None):
        self.val = val
        self.neighbors = neighbors

from typing import Optional
from collections import deque
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         oldToNew = {}
#         oldToNew[node] = Node(node.val)
#         q = deque([node])

#         while q:
#             cur = q.popleft()
#             for nei in cur.neighbors:
#                 if nei not in oldToNew:
#                     oldToNew[nei] = Node(nei.val)
#                     q.append(nei)
#                 oldToNew[cur].neighbors.append(oldToNew[nei])
#             return oldToNew[node]

            
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldToNew = {}
        def dfs(node):
            if not node:
                return None

            if node in oldToNew:
                return oldToNew[node]

            oldToNew[node] = Node(node.val)
            for nei in node.neighbors:
                dfs(nei)
                oldToNew[node].neighbors.append(dfs(nei))

            return oldToNew[node]

        return dfs(node)
