class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        
        def expand(l, r):
            cnt = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                cnt += 1
            return cnt

        for i in range(len(s)):
            cnt += expand(i, i)
            cnt += expand(i, i + 1)
        
        return cnt
        
