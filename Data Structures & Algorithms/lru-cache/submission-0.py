class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #key -> node

        #Boundaries
        self.left = Node(0, 0) #LRU end
        self.right = Node(0, 0) #MRU end
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node): #Insert at right
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key]) #Remove from current position
        self.insert(self.cache[key]) #Insert at MRU end
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #Remove old node
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node) #Insert at MRU end

        if len(self.cache) > self.capacity:
            lru = self.left.next #Least recently used
            self.remove(lru)
            del self.cache[lru.key] #Remove from hashmap
