from tools import *


class Solution(object):
    @print_
    @list_node
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        ret = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                while slow != ret:
                    slow = slow.next
                    ret = ret.next
                return ret
        return None

solution = Solution().detectCycle

l1 = ListNode(3)
l2 = ListNode(2)
l3 = ListNode(0)
l4 = ListNode(-4)

l1.next = l2
l2.next = l3
l3.next = l4

l4.next = l2
solution(head=l1)
