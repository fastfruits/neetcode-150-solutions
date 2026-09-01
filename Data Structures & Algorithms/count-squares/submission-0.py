class CountSquares:

    def __init__(self):
        self.counter = defaultdict(int) #How many times one point was added
        self.points = [] #List of all added points

    def add(self, point: List[int]) -> None:
        x, y = point
        self.counter[(x, y)] += 1
        self.points.append((x, y))

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0

        for px, py in list(self.counter.keys()):
            if px == x and py != y:
                side = abs(py - y)

                total += self.counter[(x + side, y)] * self.counter[(x + side, py)] * self.counter[(px, py)]
                total += self.counter[(x - side, y)] * self.counter[(x - side, py)] * self.counter[(px, py)]

        return total
