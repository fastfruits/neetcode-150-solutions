class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        heap = [(0, 0)] #Cost and points
        totalCost = 0

        while len(visited) < n:
            cost, node = heapq.heappop(heap)

            if node in visited:
                continue
            
            visited.add(node)
            totalCost += cost

            for neighbor in range(n):
                if neighbor not in visited:
                    x1, y1 = points[node]
                    x2, y2 = points[neighbor]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(heap, (dist, neighbor))
        
        return totalCost