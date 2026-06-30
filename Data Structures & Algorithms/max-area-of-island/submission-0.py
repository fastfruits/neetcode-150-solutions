class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxCnt = 0
        newCnt = 0

        def dfs(r, c):
            nonlocal newCnt
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0 or
                (r, c) in visited):
                return
            
            newCnt += 1
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    newCnt = 0
                    dfs(r, c)
                    maxCnt = max(maxCnt, newCnt)

        return maxCnt
                    