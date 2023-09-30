import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        r1 = ListNode(None)
        r2 = ListNode(None)
        p1 = r1
        p2 = r2
        p = head
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
                p = p.next
                p1.next = None
            else:
                p2.next = p
                p2 = p2.next
                p = p.next
                p2.next = None
        p1.next = r2.next
        return r1.next


solution = Solution().partition
solution(head=stringToListNode("[1,4,3,2,5,2]"), x=3)
solution(head=stringToListNode("[2,1]"), x=2)
solution(head=stringToListNode("[]"), x=2)
