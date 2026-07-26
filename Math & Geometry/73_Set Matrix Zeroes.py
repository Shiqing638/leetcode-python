# Methode 1: set
# Methode 2: mark

# class Solution:
#     def setZeroes(self, matrix: list[list[int]]) -> list[list[int]]:
#         row = set()
#         col = set()

#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j] == 0:
#                     row.add(i)
#                     col.add(j)

#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if i in row or j in col:
#                     matrix[i][j] = 0
#         return matrix

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> list[list[int]]:
        RowZero = False
        ColZero = False
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] == 0:
                ColZero = True

        for j in range(n):
            if matrix[0][j] == 0:
                RowZero = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if RowZero:
            for j in range(n):
                matrix[0][j] = 0
        if ColZero:
            for i in range(m):
                matrix[i][0] = 0

        return matrix
        

        

        


        


