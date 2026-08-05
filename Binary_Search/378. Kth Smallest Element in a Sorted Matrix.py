class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def countLessEqual(x):
            row = n-1
            col = 0
            cnt = 0

            while row >= 0 and col < n:
                if matrix[row][col] > x:
                    row -= 1
                else:
                    cnt += row + 1
                    col += 1
            return cnt

        left = matrix[0][0]
        right = matrix[n-1][n-1]
        while left <= right:
            mid = (left + right) // 2
            if countLessEqual(mid) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left
