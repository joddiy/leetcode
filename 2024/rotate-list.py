import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head

        def reverse(node):
            ret = ListNode(None)
            ret.next = node
            p = ret.next
            r = ret.next
            while p:
                p_ = p.next
                p.next = ret.next
                ret.next = p
                p = p_
            r.next = None
            return ret.next, r

        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        k = k % n

        l = head
        r = head
        i = 0
        while i < n - k - 1:
            r = r.next
            i += 1
        r_ = r.next
        r.next = None
        r = r_
        l, l_e = reverse(l)
        if r:
            r, _ = reverse(r)
            l_e.next = r
        t, _ = reverse(l)
        return t


solution = Solution().rotateRight
solution(head=stringToListNode("[1,2,3,4,5]"), k=2)
solution(head=stringToListNode("[0,1,2]"), k=4)
solution(head=stringToListNode("[]"), k=0)
solution(head=stringToListNode("[1]"), k=1)
solution(head=stringToListNode("[1]"), k=0)
