class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = nums[0]

        while left <= right:
            if nums[left] < nums[right]: #if already sorted leftmost is minimum
                result = min(result, nums[left])
            
            mid = (left + right) // 2
            result = min(result, nums[mid]) #get smallest

            if nums[mid] >= nums[left]: 
                left = mid + 1 #min is in the right side
            else:
                right = mid - 1 #min is in the left side
        
        return result