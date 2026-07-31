# Methode 1: heap
# Methode 2: Greedy

# Greedy
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        c = [0] * 26

        for i in range(len(tasks)):
            c[ord(tasks[i] - ord('A'))] += 1

        c.sort()

        maxi = c[25]

        idle = (maxi - 1) * n
        for i in range(24, -1, -1):
            idle -= min(maxi-1, c[i])

        return max(0, idle) + len(tasks)

# heap
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        c = Counter(tasks)
        maxHeap = [-cnt for cnt in c.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time




        



