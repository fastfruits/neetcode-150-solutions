class TimeMap:

    def __init__(self):
        self.store = {} #key -> list of (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        pairs = self.store[key]
        left = 0
        right = len(pairs) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if pairs[mid][0] <= timestamp: #timestamp early
                result = pairs[mid][1] #try going for a later one
                left = mid + 1

            else: #timestamp too big so go left
                right = mid - 1
        
        return result