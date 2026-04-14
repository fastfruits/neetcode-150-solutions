class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices): #loop through until right = lenght of prices
            if prices[right] > prices[left]: #try seeing if profit is larger
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else: #lowest value seen so make that new buy price
                left = right
            right += 1

        return maxProfit
