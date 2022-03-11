# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def t(root, depth):
            if not root:
                return depth
            depth = max(t(root.left, depth+1), t(root.right, depth+1))
            return depth
        return t(root, depth)