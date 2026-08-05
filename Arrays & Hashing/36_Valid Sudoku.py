# Methode 1: brute force
# Methode 2: hash map
# 
# class Solution:
#     def isValidSudoku(self, board: list[list[str]]) -> bool:
#         n = len(board)

#         for i in range(n):
#             visit = set()
#             for j in range(n):
#                 if board[i][j] in visit:
#                     return False
#                 if board[i][j] != ".":
#                     visit.add(board[i][j])

#         for j in range(n):
#             visit = set()
#             for i in range(n):
#                 if board[i][j] in visit:
#                     return False
#                 if board[i][j] != ".":
#                     visit.add(board[i][j])

#         for square in range(9):
#             visit = set()
#             for i in range(3):
#                 for j in range(3):
#                     row = (square//3) *3 + i
#                     col = (square%3) * 3 + j
#                     if board[row][col] in visit:
#                         return False
#                     if board[row][col] != ".":
#                         visit.add(board[row][col])
#         return True

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c%3)].add(board[r][c])
        return True

# //3：确定属于哪个 3×3 宫（宫编号）。
# %3：确定在这个 3×3 宫里的哪个位置（宫内偏移）。