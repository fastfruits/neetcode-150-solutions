class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        result = []
        i, n = 0, len(intervals)

        #Part 1 no overlap

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        #Part 2 overlap
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        #Part 3 everything after newInterval
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
