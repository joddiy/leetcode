from utils.tools import stringToListNode, ListNode


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = ListNode(None)
        p.next = head
        p_b = p
        q = p
        for _ in range(n):
            p = p.next
        while p.next:
            p = p.next
            q = q.next
        q.next = q.next.next
        return p_b.next


Solution().removeNthFromEnd(stringToListNode("[1]"), 1)
