import heapq

class Solution:
    def sss(self, points: list[list[int]], k: int) -> list[list[int]]:
        minHeap = []
        res = []
        for point in points:
            dist = self.distance(point)
            minHeap.append([dist, point])
        heapq.heapify(minHeap)

        while minHeap:
            if k > 0:
                dist, point = minHeap.heappop()
                res.append(point)
                k -= 1
            else:
                break
        return res

    def distance(self, point: list[int]):
        dis = point[0] ** 2 + point[1] ** 2
