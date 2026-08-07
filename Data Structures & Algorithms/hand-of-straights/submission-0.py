class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False #Cant be split evenly

        count = Counter(hand)
        minHeap = list(count.keys())
        heapq.heapify(minHeap) #Need access to smallest remaining

        while minHeap:
            smallest = minHeap[0]

            if count[smallest] == 0:
                heapq.heappop(minHeap) #Used remove it
                continue
            
            for card in range(smallest, smallest + groupSize):
                if count.get(card, 0) == 0:
                    return False
                count[card] -= 1
        
        return True
        