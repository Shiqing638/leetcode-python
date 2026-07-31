# Methode 1: DFS
# Methode 2: union find
# class Solution:
#     def validTree(self, n: int, edges: list[list[int]]) -> bool:
#         if len(edges) != n-1:
#             return False

#         adj = [[] for _ in range(n)]
#         for u, v in edges:
#             adj[u].append(v)
#             adj[v].append(u)

#         visit= set()

#         def dfs(node, par):
#             if node in visit:
#                 return False

#             visit.add(node)

#             for nei in adj[node]:
#                 if nei == par:
#                     continue
#                 if not dfs(nei, node):
#                     return False
#             return True

#         return dfs(0, -1) and len(visit) == n
        
             
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        parents = [i for i in range(n)]

        def find(x):
            if x != parents[x]:
                parents(x) = find(parents(x))
            return parents[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False

            parents[rootA] = rootB

            return True

        for a, b in edges:
            if not union(a,b):
                return False

        return True
