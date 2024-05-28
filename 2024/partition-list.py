import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        g = ListNode(None)
        g_e = g
        l = ListNode(None)
        l_e = l
        p = head
        while p:
            p_ = p.next
            p.next = None
            if p.val >= x:
                g_e.next = p
                g_e = g_e.next
            else:
                l_e.next = p
                l_e = l_e.next
            p = p_
        l_e.next = g.next
        return l.next


solution = Solution().partition
solution(head=stringToListNode("[1,4,3,2,5,2]"), x=3)
solution(head=stringToListNode("[2,1]"), x=2)
solution(head=stringToListNode("[]"), x=2)
