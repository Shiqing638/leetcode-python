class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        m = len(intervals)
        res = []

        for i in range(m):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                newInterval = intervals[i]
            else:
                newInterval = [min(intervals[i][0],newInterval[0]), max(intervals[i][1], newInterval[1])]
        res.append(newInterval)

        return res