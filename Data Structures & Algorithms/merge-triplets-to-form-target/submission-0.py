class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        achieved = set() #Tracks which positions can be obtained

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
        
            for i in range(3):
                if triplet[i] == target[i]:
                    achieved.add(i)
        
        return len(achieved) == 3

        