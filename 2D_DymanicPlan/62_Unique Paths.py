# Methode 1: DFS + memo
# Methode 2: DP
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         memo = {}
#         res = 0
#         def dfs(i, j):

#             if i >= m or j >= n:
#                 return 0

#             if i  == m - 1 or j == n-1:
#                 return 1

#             if (i, j) in memo:
#                 return memo[(i,j)]
            
#             memo[(i, j)] = dfs(i+1, j) + dfs(i, j+1)

#             return memo[(i,j)]

#         return dfs(0,0)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * (m+1) for _ in range(n+2)]
        for i in range(m+1):
            dp[i][n] = 0

        for j in range(n+1):
            dp[m][j] = 0

        for i in range(m):
            dp[i][n-1] = 1

        for j in range(n):
            dp[m-1][j] = 1

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]
