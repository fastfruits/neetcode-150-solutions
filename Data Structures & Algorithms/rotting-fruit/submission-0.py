class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        maxSec = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = dr + r, dc + c

                if(0 <= nr < rows and
                   0 <= nc < cols and
                   grid[nr][nc] == 1):
                   grid[nr][nc] = grid[r][c] + 1
                   maxSec = max(maxSec, grid[nr][nc])
                   queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1 
                    
        return maxSec - 2 if maxSec > 0 else 0