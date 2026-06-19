class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        numMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(current, index):
            if index == len(digits):
                result.append("".join(current))
                return

            for letter in numMap[digits[index]]:
                current.append(letter)
                backtrack(current, index + 1)
                current.pop()

        backtrack([], 0)
        return result