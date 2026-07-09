class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Cycle detection problem

        adjecencyList = defaultdict(list)
        for course, prereq in prerequisites:
            adjecencyList[course].append(prereq)

        
        visiting = set()
        visited = set()

        def dfs(node):
            if node in visiting:
                return False #Cycle
            if node in visited:
                return True #Already checked

            visiting.add(node)

            for prereq in adjecencyList[node]:
                if not dfs(prereq):
                    return False

            visiting.remove(node)
            visited.add(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True