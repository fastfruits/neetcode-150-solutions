class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if tokens == '':
            return 0
        
        stack = []
        operators = {'+', '-', '*', '/'}

        for i in tokens:
            if i in operators:
                b, a = stack.pop(), stack.pop()
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)
                elif i == '*':
                    stack.append(a * b)
                elif i == '/':
                    stack.append(int(a / b))
            else:
                stack.append(int(i))
        
        return stack[0]