class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a) #Since undirected add both directions

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            return True

        return dfs(0, -1) and len(visited) == n