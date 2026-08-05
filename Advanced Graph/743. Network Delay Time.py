from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dict = defaultdict(list)
        for u, v, w  in times:
            dict[u].append([v, w])

        minheap = [(0, k)] # dist, node
        time = 0
        visit = set()

        while minheap:
            w1, node = heapq.heappop(minheap)
            if node in visit:
                continue
            visit.add(node)
            time = max(w1, time)
                
            for nei, w2 in dict[node]:
                if nei in visit:
                    continue
                heapq.heappush(minheap, (w1+w2, nei))
        return time if len(visit) == n else -1



