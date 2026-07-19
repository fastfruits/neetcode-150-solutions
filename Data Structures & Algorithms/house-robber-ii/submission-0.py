class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def robRange(houses):
            prev2, prev1 = 0, 0
            for num in houses:
                curr = max(num + prev2, prev1)
                prev2 = prev1
                prev1 = curr
            return prev1
        
        return max(nums[0],
            robRange(nums[:-1]),
            robRange(nums[1:]))