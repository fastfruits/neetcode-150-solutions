class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        left = 0
        right = len(nums) - 1

        nums.sort() # sort array

        for i, val in enumerate(nums):
            if nums[i] > 0: # if > 0 then just end
                break
            if i > 0 and nums[i] == nums[i - 1]: # if duplicate numbers skip
                continue

            left = i + 1
            right = len(nums) - 1
            target = -nums[i] 

            while left < right:
                if nums[left] + nums[right] == target:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]: # skip duplicates on both sides
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1 

                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1  
            
        return results