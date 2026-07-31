# Methode 1: brute force
# Methode 2: 

# class Solution:
#     def maxProduct(self, nums: list[int]) -> int:
#         res = nums[0]

#         for i in range(len(nums)):
#             cur = nums[i]
#             res = max(res, cur)
#             for j in range(i+1, len(nums)):
#                 cur *= nums[j]
#                 res = max(res, cur)

#         return res
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin = 1
        curMax = 1

        for num in nums:
            tmp = curMax * num
            curMax = max(num, num*curMax, num*curMin)
            curMin = min(num, tmp, num*curMin)
            res = max(curMax, res)
        return res