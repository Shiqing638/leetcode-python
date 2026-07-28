# Methode 1: Greedy
# Methode 2: DP

#1:
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         res = nums[0]
#         cur = nums[0]

#         for i in range(1, len(nums)):
#             cur = max(nums[i], cur + nums[i])
#             res = max(re, cur)

#         return res

#2 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])

        return max(dp)