# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         memo = {}

#         def dfs(i, cur):
#             if i >= len(nums):
#                 if cur == target:
#                     return 1
#                 else:
#                     return 0

#             if (i, cur) in memo:
#                 return memo[(i,cur)]

#             memo[(i,cur)] = dfs(i+1, cur-nums[i]) + dfs(i+1, cur+nums[i])
#             return memo[(i, cur)]
         
#         return dfs(0,0)
            

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if total < abs(target):
            return 0

        if (total + target) % 2 != 0:
            return 0

        subset = (total + target) // 2

        dp = [0] * (subset +1)
        dp[0] = 1

        for num in nums:
            for s in range(subset, num-1, -1):
                dp[s] += dp[s-num]

        return dp[subset]

#原来能组成 s-num 的所有方案，把当前 num 放进去之后，都能组成 s，所以把这些方案数累加到 dp[s]