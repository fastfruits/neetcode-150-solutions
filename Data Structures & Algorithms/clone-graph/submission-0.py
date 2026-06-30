"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        hashmap = {} #Original to clone

        def dfs(node):
            if node in hashmap:
                return hashmap[node] #Already in there
            
            clone = Node(node.val)
            hashmap[node] = clone #Store before recursing

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
