# Methode 1: dfs
# Methode 2: bfs

# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         visit = set()
#         cycle = set()
#         output = []

#         preCourse = {c: [] for c in range(numCourses)}
#         for crs, pre in prerequisites:
#             preCourse[crs].append(pre)

#         def dfs(crs):
#             if crs in visit:
#                 return True

#             if crs in cycle:
#                 return False

#             cycle.add(crs)
#             for pre in preCourse[crs]:
#                 if not dfs(pre):
#                     return False
            
#             cycle.remove(crs)
#             visit.add(crs)
#             output.append(crs)
#             return True

#         for c in range(numCourses):
#             if not dfs(c):
#                 return []
#         return output
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit = set()
        cycle = set()
        output = []
        indegree = [0] * numCourses

        preCourse = [[] for c in range(numCourses)]
        for crs, pre in prerequisites:
            indegree[crs] += 1
            preCourse[pre].append(crs)

        q = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)

        while q:
            cur = q.popleft()
            output.append(cur)

            for crs in preCourse[cur]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)
        return output