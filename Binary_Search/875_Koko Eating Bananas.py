# Methode 1: brute force


import math
# class Solution:
#     def minEatingSpeed(self, piles: list[int], h: int) -> int:
#         speed = 1
#         while True:
#             time = 0
#             for pile in piles:
#                 time += math.ceil(pile/speed)
#             if time <= h:
#                 return speed
#             speed += 1

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = 0

        while left <= right:
            mid = (left + right) // 2
            time = 0

            for pile in piles:
                time += math.ceil(pile/mid)
            if time <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res


