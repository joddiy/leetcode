from tools import *
import time


class Solution(object):
    @print_
    @list_node
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        p, q = headA, headB

        # len is equal, found at first iteration
        # len not equal, found at second iteration
        while p is not q:
            if not p:
                p = headB
            else:
                p = p.next
            if not q:
                q = headA
            else:
                q = q.next
       
        return q


solution = Solution().getIntersectionNode

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)
l8 = ListNode(8)

l1.next = l2
l2.next = l3
l3.next = l7

l4.next = l5
l5.next = l6
l6.next = l7

l7.next = l8

solution(headA=l1, headB=l4)
