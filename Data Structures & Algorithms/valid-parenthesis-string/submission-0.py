class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0 #Range of possibilities

        for char in s:
            if char == '(':
                lo += 1
                hi += 1
            if char == ')':
                lo -= 1
                hi -= 1
            if char == '*':
                lo -= 1
                hi += 1
            
            if hi < 0:
                return False
            
            lo = max(lo, 0)
        
        return lo == 0