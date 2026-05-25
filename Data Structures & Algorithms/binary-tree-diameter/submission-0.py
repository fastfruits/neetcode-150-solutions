# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0] #Use list so inner function can modify

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            diameter[0] = max(diameter[0], left + right) #Update max diameter

            return 1 + max(left, right) #Return height to parent

        dfs(root)
        return diameter[0]