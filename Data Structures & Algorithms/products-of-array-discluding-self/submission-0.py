class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            products[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= postfix
            postfix *= nums[i]
        
        return products

        
                 