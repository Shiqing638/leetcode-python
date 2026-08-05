import math
class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        n = len(arr)
        minheap = []
        for i in range(n):
            if i + 1 < n:
                diff = abs(arr[i+1] - arr[i])
                heapq.heappush(minheap, (diff, arr[i], arr[i+1]))
        
        a, b, c = heapq.heappop(minheap)
        res = []
        res.append([b,c])
        
        while minheap:
            a2, b2, c2 = heapq.heappop(minheap)
            if a2 == a:
                res.append([b2,c2])
            else:
                break
        return res

        
