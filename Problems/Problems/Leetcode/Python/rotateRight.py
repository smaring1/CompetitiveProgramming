class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
		
		#find length
        size = 1
        cur = head
        while cur.next:
            size += 1
            cur = cur.next
        if k % size == 0:
            return head
        tail = cur
        cur = head
        for i in range(size - k % size - 1):
            cur = cur.next
        tail.next = head
        new_head = cur.next
        cur.next = None
        return new_head