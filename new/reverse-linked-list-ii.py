import math
import pprint
from tools import *
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
        p = ListNode(None)
        r = p
        p.next = head
        i = 0
        while i < left - 1:
            p = p.next
            i += 1
        q = p.next
        j = 0
        while j < right - left:
            t = q.next
            q.next = q.next.next
            t.next = p.next
            p.next = t
            j += 1
        return r.next


solution = Solution().reverseBetween
solution(head=stringToListNode("[1,2,3,4,5]"), left=2, right=4)
solution(head=stringToListNode("[5]"), left=1, right=1)
solution(head=stringToListNode("[3,5]"), left=1, right=2)
