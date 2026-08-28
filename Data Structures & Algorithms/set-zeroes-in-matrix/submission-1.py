class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        firstRZ = any(matrix[0][j] == 0 for j in range(col))
        firstCZ = False
        
        for i in range(row):
            if matrix[i][0] == 0:
                firstCZ = True

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if firstRZ:
            for j in range(col):
                matrix[0][j] = 0
            
        if firstCZ:
            for i in range(row):
                matrix[i][0] = 0

        