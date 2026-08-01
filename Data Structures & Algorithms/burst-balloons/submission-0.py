class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(n - length):
                right = left + length

                #Try every ballon in (left, right) as the last one popped
                for i in range(left + 1, right):
                    coins = nums[left] * nums[i] * nums[right]
                    coins += dp[left][i] #Best result left side
                    coins += dp[i][right] #Best result right side

                    dp[left][right] = max(dp[left][right], coins)
        return dp[0][n - 1]