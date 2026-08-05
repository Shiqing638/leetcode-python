# Methode 1: DFS
# Methode 2: BFS

# class Solution:
#     def numIslands(self, grid: list[list[str]]) -> int:
#         m = len(grid)
#         n = len(grid[0])

#         def dfs(i, j):
#             if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != "1":
#                 return 

#             grid[i][j] = "2"

#             dfs(i+1, j)
#             dfs(i-1, j)
#             dfs(i, j+1)
#             dfs(i, j-1)


#         res = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "1":
#                     if dfs(i, j):
#                         res += 1
#         return res
from collections import deque
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        directions = [[1,0], [-1,0], [0, 1], [0, -1]]
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != "1":
                    continue

                res += 1
                grid[i][j] = "2"
                q.append((i,j))
                while q:
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr = dr + r
                        nc = dc + c
                        if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] != "1":
                            continue
                        grid[nr][nc] = "2"
                        q.append((nr,nc))

        return res 

