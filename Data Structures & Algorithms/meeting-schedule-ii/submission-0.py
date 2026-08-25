"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        rooms = 0
        maxRooms = 0
        sPointer = ePointer = 0

        while sPointer < len(intervals):
            if starts[sPointer] < ends[ePointer]:
                rooms += 1
                sPointer += 1
            else:
                rooms -= 1
                ePointer += 1
            
            maxRooms = max(rooms, maxRooms)
        
        return maxRooms