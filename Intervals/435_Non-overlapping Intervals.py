# Methode 1:
# Methode 2:

#1 
# class Solution:
#     def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
#         intervals.sort(key=lambda x: x[1])
#         end = intervals[0][1]
#         res = 0

#         for i in range(1, len(intervals)):
#             if intervals[i][0] < end:
#                 res += 1
#             else:
#                 end = intervals[i][1]
#         return res

# 2
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        end =  intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                res += 1
                end = min(end, intervals[i][1])
            else:
                end = intervals[i][1]
        return res