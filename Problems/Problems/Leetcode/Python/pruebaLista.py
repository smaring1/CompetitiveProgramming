# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def maximumList(head):
    if head:
        maximum = head.val
        while head:
            if head.val > maximum:
                maximum = head.val
            head = head.next
        return maximum
    else:
        return 0

l1 = ListNode()
l1.val = 1
l1.next = ListNode()
l1.next.val = 2
l1.next.next = ListNode()
l1.next.next.val = 3

print(maximumList(l1))
