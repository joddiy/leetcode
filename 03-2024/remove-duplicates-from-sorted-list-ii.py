import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        r = ListNode(None)
        r.next = head
        p = r
        while p:
            t = p.next
            while t and t.next and t.val == t.next.val:
                t = t.next
            if t is not p.next:
                p.next = t.next
                t.next = None
            else:
                p = p.next
        return r.next


solution = Solution().deleteDuplicates
solution(head=stringToListNode("[1,2,3,3,4,4,5]"))
solution(head=stringToListNode("[1,1,1,2,3]"))
solution(head=stringToListNode("[1]"))
