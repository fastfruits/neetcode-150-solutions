class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures) #sets default 0

        for i in range(len(temperatures)): #loops through temperatures
            while stack and temperatures[stack[-1]] < temperatures[i]: #while current temp is warmer then top of stack
                id = stack.pop() #pop colder day
                answer[id] = i - id #distance from day to current day
            stack.append(i) 
        
        return answer