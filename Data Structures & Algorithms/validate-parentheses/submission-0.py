class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { ')': '(', '}': '{', ']': '['}

        for c in s:
            if c in mapping: #is a closing bracket
                if not stack or stack[-1] != mapping[c]:
                    return False
                stack.pop() #remove from stack
            else:
                stack.append(c)

        return len(stack) == 0