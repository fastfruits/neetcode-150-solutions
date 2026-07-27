class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if sum(nums) % 2 == 1:
            return False
        
        target = total // 2
        dp = {0}

        for num in nums:
            newDp = dp.copy()
            for s in dp:
                if s + num == target:
                    return True
                if s + num < target:
                    newDp.add(s + num)
            dp = newDp
        
        return target in dp