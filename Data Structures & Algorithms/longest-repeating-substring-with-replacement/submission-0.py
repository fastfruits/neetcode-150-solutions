class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxLen = 0
        count = {}
        maxFreq = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1 #get next right
            maxFreq = max(maxFreq, count[s[right]]) #gets most frequent char

            if (right - left + 1) - maxFreq > k: #if need too many replacements move left + 1
                count[s[left]] -= 1
                left += 1
            
            maxLen = max(maxLen, right - left + 1)

        return maxLen