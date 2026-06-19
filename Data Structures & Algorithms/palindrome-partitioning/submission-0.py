class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrome(sub):
            return sub == sub[::-1] #Compare strings
        
        def backtrack(start, current):
            if start == len(s):
                result.append(current[:])
                return

            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if isPalindrome(sub):
                    current.append(sub)
                    backtrack(end, current)
                    current.pop()
        
        backtrack(0, [])
        return result