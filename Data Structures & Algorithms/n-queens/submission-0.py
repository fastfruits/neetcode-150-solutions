class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()
        negDiag = set()

        result = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row + col) in posDiag or (row - col) in negDiag:
                    continue #Cant place skip


                cols.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)
                board[row][col] = "."

        backtrack(0)
        return result