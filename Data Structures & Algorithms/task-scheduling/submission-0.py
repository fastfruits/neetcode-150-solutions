class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        f = max(count.values()) #Highest frequencies
        max_count = sum(1 for v in count.values() if v == f) #Tasks with max freq

        return max(len(tasks), (f - 1) * (n + 1) + max_count)