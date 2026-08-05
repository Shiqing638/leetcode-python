# Methode 1: DFS
# Methode 2: BFS
# Methode 3: union find
# class Solution:
#     def countComponents(self, n: int, edges: list[list[int]]) -> int:
#         dict = collections.defaultdict(list)

#         for u, v in edges:
#             dict[u].append(v)
#             dict[v].append(u)

#         visit = set()

#         def dfs(node):
#             if node in visit:
#                 return

#             visit.add(node)
            
#             for nei in dict[node]:
#                 dfs(nei)

#         res = 0

#         for i in range(n):
#             if i not in visit:
#                 dfs(i)
#                 res += 1
#         return res

# from collections import defaultdict, deque
# class Solution:
#     def countComponents(self, n: int, edges: list[list[int]]) -> int:
#         dict = defaultdict(list)
#         for u, v in edges:
#             dict[u].append(v)
#             dict[v].append(u)

#         visit = set()

#         for i in range(n):
#             if i in visit:
#                 return
#             q = deque()
#             q.append(i)
#             visit.add(i)
#             while q:
#                 for nei in dict[i]:
#                     if nei in visit:
#                         return 
#                     visit.add(nei)
#                     q.append(nei)
#             res += 1
#         return res
                
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parents = [i for i in range(n)]

        def find(x):
            if x != parents[x]:
                parents[x] = parents[parents[x]]
            return parents[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA == rootB:
                return 0
            parents[rootB] = rootA
            return 1

        res = n

        for a,b in edges:
            res -= union(a,b)

        return res
        
