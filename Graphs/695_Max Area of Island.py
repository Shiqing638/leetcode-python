class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >=n or grid[i][j] != 1:
                return 0

            grid[i][j] = "#"

            return (1+dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1))


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i,j)) 
        return res
        