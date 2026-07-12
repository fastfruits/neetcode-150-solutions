class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for source, destination in sorted(tickets, reverse=True): 
            adj[source].append(destination)
        
        result = []

        def dfs(airport):
            while adj[airport]:
                next_dest = adj[airport].pop() #Smallest lexical destination
                dfs(next_dest)
            result.append(airport) #No other destinations
        
        dfs("JFK")
        return result[::-1]