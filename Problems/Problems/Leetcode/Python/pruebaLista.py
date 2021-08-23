# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode()
    cur = dummy
    carry = 0
    while l1 or l2:
        if l1:
            x = l1.val
        else:
            x = 0
        if l2:
            y = l2.val
        else:
            y = 0
        suma = carry + x + y
        carry = suma // 10
        cur.next = ListNode(val=suma%10)
        cur = cur.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if carry > 0:
        cur.next = ListNode(val=carry)
    return dummy.next

l1 = ListNode()
l1.val = 2
l1.next = ListNode()
l1.next.val = 4
l1.next.next = ListNode()
l1.next.next.val = 3

l2 = ListNode()
l2.val = 5
l2.next = ListNode()
l2.next.val = 6
l2.next.next = ListNode()
l2.next.next.val = 4

result = addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
