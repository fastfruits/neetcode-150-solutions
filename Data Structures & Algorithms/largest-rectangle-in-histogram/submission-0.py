class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights): #loop through heights with index and height
            start = i #farthest left

            while stack and stack[-1][1] > h: #pop taller bars that cant go right anymore
                id, height = stack.pop()
                maxArea = max(maxArea, height * (i - id))
                start = id  #current bar goes to popped bar's index
            stack.append((start, h))

        
        for id, height in stack: #get remaining bars in stack that extend to the end
            maxArea = max(maxArea, height * (len(heights) - id))

        return maxArea