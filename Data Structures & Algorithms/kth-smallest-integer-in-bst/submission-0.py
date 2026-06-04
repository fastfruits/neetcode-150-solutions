# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.n = 0
        self.result = 0

        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)

            self.n += 1
            if self.n == k:
                self.result = node.val
                return

            dfs(node.right)
        
        dfs(root)
        return self.result