# Methode 1: DFS
# Methode 2: BFS

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
#         visit = set()
#         cycle = set()
#         preCourse = {c: [] for c in range(numCourses)}
#         for crs, pre in prerequisites:
#             preCourse[crs].append(pre)

#         def dfs(crs):
#             if crs in cycle:
#                 return False
#             if crs in visit:
#                 return True

#             cycle.add(crs)
#             for pre in preCourse[crs]:
#                 if not dfs(pre):
#                     return False
#             visit.add(crs)
#             cycle.remove(crs)
#             return True

#         for c in range(numCourses):
#             if not dfs(c):
#                 return False
#         return True

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree = [0] * numCourses
        preCourses = [[] for i in range(numCourses)]
        finish = 0

        for crs, pre in prerequisites:
            indegree[crs] += 1 # how many pre course for crs
            preCourses[pre].append(crs)

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            cur = q.popleft()
            finish += 1
            for crs in preCourses[cur]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)

        return finish == numCourses


        