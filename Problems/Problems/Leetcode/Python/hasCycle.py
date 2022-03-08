# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            cur = head
            nodes = set()
            while cur.next:
                if cur not in nodes:
                    nodes.add(cur)
                else:
                    return True
                cur = cur.next
        return False