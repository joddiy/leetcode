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
        q = p
        while p and q and q.next:
            p = p.next
            q = q.next.next
            if p is q:
                return True
        return False


solution = Solution().hasCycle
solution(head=stringToListNode("[3,2,0,-4]"), pos=1)
