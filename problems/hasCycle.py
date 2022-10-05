from tools import *


class Solution(object):
    @print_
    @list_node
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p, q = head, head
        while p and q and q.next:
            p = p.next
            q = q.next.next
            if p == q:
                return True
        return False


solution = Solution().hasCycle