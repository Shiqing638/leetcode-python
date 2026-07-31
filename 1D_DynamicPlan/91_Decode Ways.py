# Methode 1: DP
# Methode 2: DFS + memo

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         n = len(s)
#         dp = [0] * (n+1)
#         dp[n] = 1

#         for i in range(n-1, -1, -1):
#             if s[i] == "0":
#                 dp[i] = 0
#                 continue

#             dp[i] = dp[i+1]

#             if(
#                 i + 1 < n and 
#                 (s[i] == "1" or (s[i] == "2" and s[i+1] <= "6"))
#             ):
#                 dp[i] += dp[i+2]
#         return dp[0]

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def dfs(i):
            if i > len(s):
                return 1

            if i in memo:
                return memo[i]

            memo[i] = dfs(i+1)
            if(
                i + 1 < n and 
                (s[i] == "1" or (s[i] == "2" and s[i+1] <= "6"))             
            ):
                memo[i] += dfs(i+2)

            return memo[i]

        return dfs(0)
