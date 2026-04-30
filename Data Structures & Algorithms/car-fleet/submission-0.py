class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted(zip(position, speed), reverse=True) #pair position + speed sorted by closest to target

        for p, s in pairs:
            time = (target - p) / s #time to get to target
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]: #if current car is faster than the fleet ahead merge
                stack.pop()

        return len(stack)


