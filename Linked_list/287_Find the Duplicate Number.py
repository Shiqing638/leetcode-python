# Methode 1: hash set
# Methode 2: fast slow pointer

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         visit = set()
#         for num in nums:
#             if num not in visit:
#                 visit.add(num)
#             else:
#                 return num

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        ptr1 = 0
        ptr2 = slow

        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr2