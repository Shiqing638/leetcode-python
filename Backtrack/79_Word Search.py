class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i, j, w):
            if w >= len(word):
                return True
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[i] or board[i][j] == "#":
                return False

            board[i][j] = "#"

            res = dfs(i+1, j, w+1) or dfs(i-1, j, w+1) or dfs(i, j+1, w+1) or dfs(i, j-1, w+1)

            board[i][j] = word[w]

            return res

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False
        

