from tools import *


class Solution(object):
    @print_
    @list_node
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        i, j = head, head.next
        while j and j.next:
            # pick the odd node from j+1
            k = j.next
            j.next = j.next.next
            # add to the end of i
            k.next = i.next
            i.next = k
            # next
            i = i.next
            j = j.next
        return head


solution = Solution().oddEvenList

solution("[1,2,3,4,5]")