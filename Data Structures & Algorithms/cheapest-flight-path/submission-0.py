class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for u, v, price in flights:
                if prices[u] == float('inf'):
                    continue
                tmpPrices[v] = min(tmpPrices[v], prices[u] + price)
            
            prices = tmpPrices
        
        return -1 if prices[dst] == float('inf') else prices[dst]