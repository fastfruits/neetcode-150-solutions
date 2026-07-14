class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        heap = [(grid[0][0], 0, 0)]

        while heap:
            t, r, c = heapq.heappop(heap)

            if (r, c) == (n - 1, n - 1):
                return t
            
            if (r, c) in visited:
                continue
            
            visited.add((r, c))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < n and
                    0 <= nc < n and
                    (nr, nc) not in visited):
                    new_t = max(t, grid[nr][nc])
                    heapq.heappush(heap, (new_t, nr, nc))

        return -1