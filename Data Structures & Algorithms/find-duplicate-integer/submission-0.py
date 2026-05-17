class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        #Part one find intersection in cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0
        #Part two find begining of cycle
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow


