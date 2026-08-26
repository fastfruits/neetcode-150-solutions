class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort(key=lambda x: x[0])
        sortedQ = sorted(range(len(queries)), key=lambda i: queries[i])

        result = [-1] * len(queries)
        heap = []
        i = 0

        for q in sortedQ:
            qi = queries[q]

            while i < len(intervals) and intervals[i][0] <= qi:
                start, end = intervals[i]

                heapq.heappush(heap, (end - start + 1, end))
                i += 1

            while heap and heap[0][1] < qi:
                heapq.heappop(heap)

            if heap:
                result[q] = heap[0][0]

        return result

