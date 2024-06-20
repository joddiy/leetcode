import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        ret = ListNode(None)
        ret.next = head
        l = r = ret
        i = 0
        while i < left - 1:
            i += 1
            l = l.next
        i = 0
        while i < right + 1:
            i += 1
            r = r.next
        p = l.next
        l_e = l.next
        i = 0
        while i < right - left + 1:
            i += 1
            p_ = p.next
            p.next = l.next
            l.next = p
            p = p_
        l_e.next = r
        return ret.next


solution = Solution().reverseBetween
solution(head=stringToListNode("[1,2,3,4,5]"), left=2, right=4)
solution(head=stringToListNode("[5]"), left=1, right=1)
