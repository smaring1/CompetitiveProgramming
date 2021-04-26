# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        size = 0
        cur = head
        while cur:
            cur = cur.next
            size += 1
        print(size)
        medium = size // 2
        cont = 0
        cur1 = head
        while cur1:
            if cont == medium:
                return cur1
            cur1 = cur1.next
            cont += 1