class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        have = {}
        formed = 0
        left = 0
        minLen = float('inf')
        result = (-1, -1)

        for right in range(len(s)):
            c = s[right]
            have[c] = have.get(c, 0) + 1
        
            if c in need and have[c] == need[c]:
                formed += 1
            
            while formed == len(need):
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    result = (left, right)
                
                have[s[left]] -= 1
                
                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1
        
        return s[result[0]: result[1] + 1] if minLen != float('inf') else ""