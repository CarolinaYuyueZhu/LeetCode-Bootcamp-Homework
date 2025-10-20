# 73: Set Matrix Zeros
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # m * n size matrix
        m, n = len(matrix), len(matrix[0])
        # use set() because we only care which rows and columns contain at least one zero
        # if another zero appears in the same row or column, already marked, does not change the result
        row, column = set(), set()
        # find places where zero occurs
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)
        # replace each row with zero
        for i in row:
            for j in range(n):
                matrix[i][j] = 0
        # replace each column with zero
        for j in column:
            for i in range(m):
                matrix[i][j] = 0
