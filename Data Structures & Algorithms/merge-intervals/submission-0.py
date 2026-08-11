class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = result[-1][1]

            if start <= lastEnd: #Overlap most recent
                result[-1][1] = max(lastEnd, end)
            else: #No overlap
                result.append([start,end])

        return result