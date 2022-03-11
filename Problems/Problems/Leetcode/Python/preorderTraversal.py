# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        def t(root, sol):
            if root:
                sol.append(root.val)
                t(root.left, sol)
                t(root.right, sol)
            return sol
        sol = t(root, sol)
        return sol