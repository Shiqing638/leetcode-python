# Methode 1: DP
# Methode 2: DFS + memo


# class Solution:
#     def rob(self, nums: list[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]

#         def robber(nums):
#             dp = [0] * (len(nums) +2)

#             for i in range(len(nums)-1, -1, -1):
#                 dp[i] = max(dp[i+2] + nums[i], dp[i+1])

#             return dp[i]

#         return max(robber(nums[:-1]), robber(nums[1:]))

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.robber(nums[:-1]), self.robber(nums[1:]))


    def robber(self, nums):
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(dfs(i+2)+nums[i], dfs(i+1))

            return memo[i]
        return dfs(0)

