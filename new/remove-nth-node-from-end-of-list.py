import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        r = ListNode(None)
        r.next = head
        p = q = r
        i = 0
        while i < n + 1:
            q = q.next
            i += 1

        while q:
            p = p.next
            q = q.next

        p.next = p.next.next
        return r.next


solution = Solution().removeNthFromEnd
solution(head=stringToListNode("[1,2,3,4,5]"), n=2)
solution(head=stringToListNode("[1]"), n=1)
solution(head=stringToListNode("[1,2]"), n=1)
