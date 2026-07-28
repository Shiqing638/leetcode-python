from collections import deque

class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> list[list[int]]:
        m = len(rooms)
        n = len(rooms[0])

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        q = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j))

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                if rooms[nr][nc] != 2147483647:
                    continue

                rooms[nr][nc] = rooms[r][c] + 1
                q.append((nr, nc))
        return rooms