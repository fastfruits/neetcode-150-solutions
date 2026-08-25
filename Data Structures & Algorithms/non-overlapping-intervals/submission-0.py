class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1]) #Sort by end time

        lastEnd = float('-inf')
        count = 0

        for start, end in intervals: #Overlaps the interval
            if start < lastEnd:
                count += 1
            else: #No overlap
                lastEnd = end
        
        return count