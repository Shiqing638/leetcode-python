# Methode 1: DFS + memo
# Methode 2: DP

# class Solution:
#     def rob(self, nums: list[int]) -> int:
#         memo = {}

#         def dfs(i):
#             if i >= len(nums):
#                 return 0

#             if i in memo:
#                 return memo[i]

#             memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))

#             return memo[i]

#         return dfs(0)

class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [0] * (len(nums)+2)

        for i in range(len(nums)-1, -1, -1):
            dp[i] = max(dp[i+2] + nums[i], dp[i+1])

        return dp[0]
