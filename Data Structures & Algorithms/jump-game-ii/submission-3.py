class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        end = 0 #Farthest reach current jumps
        farthest = 0 #Farthest reach with one more jump

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == end:
                jumps += 1
                end = farthest

        return jumps