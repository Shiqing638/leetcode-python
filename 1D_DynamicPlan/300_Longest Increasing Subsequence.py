# Methode 1: 1D dynamic plan
# Methode 2: Greedy

# 1
# from bisect import bisect_left
# class Solution:
#     def lengthOfLIS(self, nums: list[int]) -> int:
#         sub = []
#         for num in nums:
#             i = bisect_left(sub, num)
#             if i == len(sub):
#                 sub.append(num)
#             else:
#                 sub[i] = num
#         return len(sub)

# 2
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
nums = [10,9,2,5,3,7,101,18]
sol = Solution()
print(sol.lengthOfLIS(nums))