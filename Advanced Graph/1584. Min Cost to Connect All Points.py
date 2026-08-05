import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minheap = [(0,0)] # cost, point index
        visit = set()
        res = 0

        while minheap:
            cost, index = heapq.heappop(minheap)
            if index in visit:
                continue

            visit.add(index)

            res += cost
            x1, y1 = points[index]
            for j in range(n):
                if j not in visit:
                    x2, y2 = points[j]
                    dist = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(minheap, (dist, j))
        return res if len(visit) == n else -1
