# Methode 1: n & 1
# Methode 2: n & (n-1)
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         ans = 0
#         while n:
#             ans += n & 1
#             n >> 1
#         return ans

    
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= (n-1)
            ans += 1

        return ans
