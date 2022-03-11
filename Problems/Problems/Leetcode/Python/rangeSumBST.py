# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        acum = 0
        def t(root, acum, low, high):
            if root:
                if low <= root.val <= high:
                    acum += root.val
                acum = t(root.left, acum, low, high)
                acum = t(root.right, acum, low, high)
            return acum
        
        
        return t(root, acum, low, high)