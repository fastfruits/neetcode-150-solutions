class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = [0] * 26
        s2Count = [0] * 26
        
        for c in s1:
            s1Count[ord(c) - ord('a')] += 1 #get ASCII values of chars
        
        for right in range(len(s2)):
            s2Count[ord(s2[right]) - ord('a')] += 1 #get ASCII values of chars in s2 window

            if right >= len(s1): # if right too big and not found yet shift right
                s2Count[ord(s2[right - len(s1)]) - ord('a')] -= 1 
            
            if s1Count == s2Count: #compare lists 
                return True

        return False