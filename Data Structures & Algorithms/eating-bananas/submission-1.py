class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = max(piles) #worst case eat fastest

        while left <= right:
            mid = (left + right) // 2

            totalHours = sum(math.ceil(pile / mid) for pile in piles) #ceil is ceiling for each pile in piles

            if totalHours > h:
                left = mid + 1 #too slow
            elif totalHours <= h:
                right = mid - 1
                result = mid #works try slower
        
        return result