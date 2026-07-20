class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = max(nums)
        curMax = curMin = 1

        for num in nums:
            if num == 0:
                curMax = curMin = 1
                continue
            
            temp = curMax
            curMax = max(num, num * curMax, num * curMin)
            curMin = min(num, num * temp, num * curMin)
            maxProduct = max(maxProduct, curMax)
    
        return maxProduct