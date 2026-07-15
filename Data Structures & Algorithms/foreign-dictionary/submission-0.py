class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w} #Each character is a node

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            
            #Edge case
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break #First difference matters

        visited = {}
        result = []

        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True

            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True #Cycle detected

            visited[char] = False #Mark visited
            result.append(char)
            return False
        
        for char in adj:
            if dfs(char):
                return ""
    
        return "".join(result[::-1])
            
