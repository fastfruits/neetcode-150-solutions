class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        heap = [(0, k)] #(Distance, node)
        dist = {}

        while heap:
            d, node = heapq.heappop(heap)

            if node in dist: #Visited
                continue 
            
            dist[node] = d

            for neighbor, weight in adj[node]:
                if neighbor not in dist:
                    heapq.heappush(heap, (d + weight, neighbor))
        
        return max(dist.values()) if len(dist) == n else -1