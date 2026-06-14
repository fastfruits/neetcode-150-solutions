class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(x**2 + y**2, x, y) for x, y in points]
        heapq.heapify(heap)

        result = []

        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])

        return result