# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val: #Both in left subtree
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right #Both in right subtree
            else:
                return curr #Current node is LCA