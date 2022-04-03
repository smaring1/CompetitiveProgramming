# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def t(root, depth):
            if not root:
                return depth
            return max(t(root.left, depth+1), t(root.right, depth+1))
        a = t(root, 0)
        sol = []
        for i in range(a):
            sol.append([])
        def dfs(root, h):
            nonlocal sol
            if not root:
                return 
            sol[h].append(root.val)
            dfs(root.left, h+1)
            dfs(root.right, h+1)
        dfs(root, 0)
        return sol