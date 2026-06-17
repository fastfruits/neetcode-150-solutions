class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(current, visited):
            if len(current) == len(nums):
                result.append(current[:])

            for i in range(len(nums)):
                if i in visited:
                    continue
                
                current.append(nums[i])
                visited.add(i)
                backtrack(current, visited)
                current.pop()
                visited.discard(i)

        backtrack([], set())
        return result

