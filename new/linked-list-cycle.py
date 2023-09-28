from tools import *
import pprint
from collections import defaultdict


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    @print_
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = pp = head
        while p and pp and p.next and pp.next and pp.next.next:
            p = p.next
            pp = pp.next.next
            if p == pp:
                return True
        return False


solution = Solution().hasCycle
