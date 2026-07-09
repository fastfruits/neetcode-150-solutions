class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Cycle detection and topological sort
        result = []

        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visiting = set()
        visited = set()

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True

            visiting.add(node)

            for prereq in adj[node]:
                if not dfs(prereq):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            result.append(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return result