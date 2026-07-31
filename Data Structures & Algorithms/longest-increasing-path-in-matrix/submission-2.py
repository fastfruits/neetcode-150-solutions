class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        sys.setrecursionlimit(100000)
        rows, cols = len(matrix), len(matrix[0])
        memoization = {}

        def dfs(r, c):
            if (r, c) in memoization:
                return memoization[(r, c)]

            best = 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and 0 <= nc < cols and
                    matrix[nr][nc] > matrix[r][c]):
                    best = max(best, 1 + dfs(nr, nc))

            memoization[(r, c)] = best
            return best
        
        return max(dfs(r, c) for r in range(rows) for c in range(cols))