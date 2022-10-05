from tools import *


class Solution(object):
    @print_
    @list_node
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ret = ListNode(None)
        ret.next = head
        fast = slow = ret
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return ret.next


solution = Solution().removeNthFromEnd

solution("[1,2,3,4,5]", 2)
solution("[1]", 1)
solution("[1,2]", 1)