class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold = [0] * n
        notHold = [0] * n

        hold[0] = -prices[0]

        for i in range(1, n):
            prevNotHold = notHold[i - 2] if i >= 2 else 0
            hold[i] = max(hold[i - 1], prevNotHold - prices[i])
            notHold[i] = max(notHold[i - 1], hold[i - 1] + prices[i])

        return notHold[-1]