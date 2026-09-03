class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = n

        for i, num in enumerate(nums):
            result ^= i ^ num #Cancel num out with current index
        
        return result