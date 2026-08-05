# Methode 1: sort
# Methode 2: heap
from collections import Counter

# class Solution:
#     def reorganizeString (self, s: str) -> str:
#         count = Counter(s) # key: char, values: times
#         n = len(s)
#         arr = []
#         for k, v in count.items():
#             arr.append([k,v])
#         arr.sort(key=lambda x: x[1], reverse=True)
#         if arr[0][1] > (n+1) // 2:
#             return ""
#         res = [""] * n
#         idx = 0

#         for ch, freq in arr:
#             while freq:
#                 if idx >= n:
#                     idx = 1
#                 res[idx] = ch
#                 freq -= 1
#                 idx += 2
#         return "".join(res)

import heapq
class Solution:
    def reorganizeString (self, s: str) -> str:
        count = Counter(s)
        n = len(s)
        maxheap = [[-value, key] for key, value in count.items()]
        heapq.heapify(maxheap)
        if maxheap[0] > (n+1)//2:
            return ""

        res = [""] * n
        idx = 0
        while maxheap:
            v, k = heapq.heappop(maxheap) # v is minus
            while v:
                if idx >= n:
                    idx = 1
                res[idx] = k
                idx += 2
                v += 1
        return "".join(res)


