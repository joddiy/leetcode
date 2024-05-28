import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = ListNode(None)
        p.next = head
        pp = p
        while p and pp and pp.next:
            p = p.next
            pp = pp.next.next
            if p == pp:
                return True
        return False


solution = Solution().hasCycle
solution(head=stringToListNode("[3,2,0,-4]"), pos=1)
