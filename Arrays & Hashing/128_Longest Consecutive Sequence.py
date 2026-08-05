# Methode 1: class Solution:
class Solution:

    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        res = 1

        for i in range(len(nums)):
            cur = 1
            for j in range(i, len(nums)):
                if j + 1 < len(nums):
                    if nums[j] + 1 == nums[j+1]:
                        cur += 1
                    elif nums[j] == nums[j+1]:
                        continue
                    else:
                        break

            res = max(res, cur)
        return res

# Methode 2: hash set

# 数据结构	是否重点	常见用途
# set	⭐⭐⭐⭐⭐	去重、visited、快速查找
# dict	⭐⭐⭐⭐⭐	映射、计数、索引
# defaultdict	⭐⭐⭐⭐⭐	图、计数、分组
# Counter	⭐⭐⭐⭐	统计频率

class Solution:

    def longestConsecutive(self, nums: list[int]) -> int:
        hashSet = set(nums)
        res = 0
    
        for num in hashSet:
            if (num-1) not in hashSet:
                cur = num
                longest = 1
                while num + 1 in hashSet:
                    longest += 1
            res = max(res, longest)

        return res
