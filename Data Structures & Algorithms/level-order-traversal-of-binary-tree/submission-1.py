# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root]) #Use queue for breadth first search
        result = []

        while queue:
            level = []
            for _ in range(len(queue)): #Check level's exact number
                node = queue.popleft()
                level.append(node.val)
    
                if node.left: queue.append(node.left) #If node exists add to queue
                if node.right: queue.append(node.right) #If node exists add to queue
            
            result.append(level)

        return result