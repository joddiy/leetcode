from utils.tools import stringToListNode, ListNode


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        meet = None
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                meet = slow
                break
        if meet:
            p = head
            q = meet
            while p and q:
                if p is q:
                    return p
                else:
                    p = p.next
                    q = q.next
        return None


head = stringToListNode("[3,2,0,-4]")
head.next.next.next.next = head.next
Solution().detectCycle(head).val
