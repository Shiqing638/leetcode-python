# Methode 1: brute force
# Methode 2: two pointer
# class Solution:
#     def twoSum(self, numbers: list[int], target: int) -> list[int]:
#         for i in range(len(numbers)):
#             res = 0
#             for j in range(i+1, len(numbers)):
#                 res = numbers[i] + numbers[j]
#                 if res > target:
#                     break
#                 elif res == target:
#                     return [i+1,j+1]
#                 else:
#                     continue
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [-1,-1]
    