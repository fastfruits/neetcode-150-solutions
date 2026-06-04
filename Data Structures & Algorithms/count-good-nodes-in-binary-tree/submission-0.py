# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxSoFar):
            if not node:
                return 0
            cnt = 1 if node.val >= maxSoFar else 0
            newMax = max(maxSoFar, node.val)

            return cnt + dfs(node.left, newMax) + dfs(node.right, newMax)
        
        return dfs(root, root.val)