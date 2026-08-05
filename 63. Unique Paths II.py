# class Solution(object):
#     def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
#         memo = {}
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
#         def dfs(i, j):
#             if i >= m or j >= n:
#                 return 0
            
#             if obstacleGrid[i][j] == 1:
#                 return 0
            
#             if i == m - 1 and j == n - 1:
#                 return 1
            
#             if (i, j) in memo:
#                 return memo[(i, j)]

#             memo[(i, j)] = dfs(i+1, j) + dfs(i, j+1)

#             return memo[(i, j)]
#         return dfs(0,0) 

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * (n+1) for _ in range(m+1)]
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        dp[m-1][n-1] = 1

        for i in range(m+1):
            dp[i][n] = 0

        for j in range(n+1):
            dp[m][j] = 0

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == m-1 and j == n-1:
                    continue
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]
