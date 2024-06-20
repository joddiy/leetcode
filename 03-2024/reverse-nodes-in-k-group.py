import math
import sys

from tools import *
import pprint
from collections import defaultdict
import heapq


class Solution(object):
    @print_
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n = 0
        p = head
        while p:
            p = p.next
            n += 1
        n = n // k * k

        i = 0
        ret = ListNode(None)
        ret.next = head
        h = ret
        t = ret.next
        p = ret.next
        while i < n and p:
            # go to next group
            if i != 0 and i % k == 0:
                h, t = t, t.next
            # pop the p
            p_next = p.next
            p.next = None
            t.next = p_next
            # insert from the head
            h_next = h.next
            h.next = p
            p.next = h_next
            # continue
            p = p_next
            i += 1

        return ret.next


solution = Solution().reverseKGroup
solution(head=stringToListNode("[1,2,3,4,5]"), k=3)
solution(head=stringToListNode("[1,2,3,4,5]"), k=2)
