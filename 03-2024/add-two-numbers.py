import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(None)
        p = ret
        c = 0
        while l1 or l2:
            if l1:
                c += l1.val
                l1 = l1.next
            if l2:
                c += l2.val
                l2 = l2.next
            p.next = ListNode(c % 10)
            p = p.next
            c = c // 10
        if c != 0:
            p.next = ListNode(c)
        return ret.next


solution = Solution().addTwoNumbers
solution(l1=stringToListNode("[2,4,3]"), l2=stringToListNode("[5,6,4]"))
solution(l1=stringToListNode("[2,4,6]"), l2=stringToListNode("[5,6,4]"))
