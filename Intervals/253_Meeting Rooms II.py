# Methode 1: heap
# Methode 2: two pointer

# import heapq
# class Solution:
#     def minMeetingRooms(self, intervals: list[list[int]]) -> int:
#         intervals.sort()
#         minHeap = []

#         for interval in intervals:
#             if minHeap and interval[0] > minHeap[0]:
#                 heapq.heappop(minHeap)
#             heapq.heappush(minHeap, interval[1])
#         return len(minHeap)

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        start = [sorted(interval[0] for interval in intervals)]
        end = [sorted(interval[1] for interval in intervals)]

        res = 0
        count = 0

        s = e = 0

        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else: 
                e += 1
                count -= 1
            res = max(res, count)
        return res
            
