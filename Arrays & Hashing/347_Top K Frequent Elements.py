# Methode 1: Counter + heap
# Methode 2: Counter + sort
# Methode 3: Bucket

# Methode 1
# from collections import Counter
# import heapq
# class Solution:
#     def topKFrequent(self, nums: list[int], k : int) -> list[int]:
#         count = Counter(nums)
#         minHeap = []
#         res = []
#         for key, value in count.items():
#             heapq.heappush(minHeap, (-value, key))
        
#         for _ in range(k):
#             v, k = heapq.heappop(minHeap)
#             res.append(k)
#         return res

# Methode 2
# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: list[int], k : int) -> list[int]:
#         count = Counter(nums)
#         items = sorted(count.items(), key=lambda x: x[1], reverse=True)
#         return [x for x, _ in items[:k]]

# Methode 3
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k : int) -> list[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        res = []
        for num, freq in count.items():
            bucket[freq].append(num)

        for freq in range(len(nums)-1, 0, -1):
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res

nums = [1,1,1,2,2,3]
k = 2
sol = Solution()
res = sol.topKFrequent(nums, k)
print (res)
    
