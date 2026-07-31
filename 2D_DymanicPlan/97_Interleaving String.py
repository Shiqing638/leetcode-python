# Methode 1: DFS + memo
# Methode 2: DP

# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         m = len(s1)
#         n = len(s2)

#         if m + n != len(s3):
#             return False

#         memo = {}

#         def dfs(i, j):
#             if i == m and j == n:
#                 return True

#             if (i, j) in memo:
#                 return memo[(i, j)]

#             k = i + j

#             if i < m and s1[i] == s3[k]:
#                 if dfs(i+1, j):
#                     memo[(i,j)] = True
#                     return True

#             if j < n and s2[j] == s3[k]:
#                 if dfs(i, j + 1):
#                     memo[(i, j)] = True
#                     return True

#             memo[(i, j)] = False
#             return False

#         return dfs(0,0)
                
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        
        # m: row, n: col
        m, n = len(s1), len(s2)

        dp = [[False] * (n+1) for _ in range(m+1)]        
        dp[m][n] = True

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    return True
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    return True
        return dp[0][0]