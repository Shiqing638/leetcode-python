# # Methode 1: DFS + parent node
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def distanceK(self, root: TreeNode, target: TreeNode,k: int) -> list[int]:
#         res = []
#         visit = set()
#         if not root:
#             return []
#         def parent(node, par):
#             if not node:
#                 return 
#             node.parent = par
#             if node.left:
#                 parent(node.left, node)
#             if node.right:
#                 parent(node.right, node)

#         parent(root, None)

#         def dfs(node, distance):
#             if not node:
#                 return
#             if node in visit:
#                 return
#             if distance == k:
#                 res.append(node.val)
#                 return

#             visit.add(node)
            
#             dfs(node.left, distance+1)
#             dfs(node.right, distance+1)
#             dfs(node.parent, distance+1)

            

#         dfs(target, 0)
#         return res

# Methode 2: DFS + graph
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode,k: int) -> list[int]:
        graph = collections.defaultdict(list)

        def graph(node, parent):
            if node and node.parent:
                graph[node.val].append(parent.val)
            if node.left:
                graph(node.left, node)
            if node.right:
                graph(node.right, node)

        graph(root, None)

        res = []
        visit = set()
        visit.add(target)

        def dfs(node, distance):
            if not node:
                return
            if node in visit:
                return
            if distance == k:
                res.append(node.val)
                return
            for nei in graph[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei, distance+1)
        dfs(target, 0)
        return res



