import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = ListNode(None)
        p.next = head
        v = t = p
        i = 0
        while i < n + 1:
            t = t.next
            i += 1
        while t:
            p = p.next
            t = t.next
        r = p.next
        p.next = p.next.next
        r.next = None
        return v.next


solution = Solution().removeNthFromEnd
solution(head=stringToListNode("[1,2,3,4,5]"), n=2)
solution(head=stringToListNode("[1]"), n=1)
solution(head=stringToListNode("[1,2]"), n=1)
