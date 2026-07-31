class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        res = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j])
                if grid[i][j] == 1:
                    fresh += 1

        while q and fresh:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append([nr, nc])
            res += 1

        return res if fresh == 0 else -1


                    
        
             