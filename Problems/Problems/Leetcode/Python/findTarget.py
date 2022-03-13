# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nodes = {}
        def t(root, nodes):
            if not root:
                return
            if root.val not in nodes:
                nodes[root.val] = 1 
            else:
                nodes[root.val] += 1
            t(root.left, nodes)
            t(root.right, nodes)
        t(root, nodes)
        for i in nodes:
            sub = k - i
            if sub in nodes and sub != i:
                    return True
            if sub in nodes and sub == i:
                if nodes[sub] > 1:
                    return True
        return False