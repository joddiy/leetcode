import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        # get the list length
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        k = k % n

        if k == 0:
            return head

        # get the last kth node
        p = head
        i = 0
        while i < n - k - 1:
            p = p.next
            i += 1

        # put the last kth nodes at the head
        ret = ListNode(None)
        ret.next = p.next
        p.next = None

        q = ret.next
        while q.next:
            q = q.next
        q.next = head

        return ret.next


solution = Solution().rotateRight
solution(stringToListNode("[1,2,3,4,5]"), k=2)
solution(stringToListNode("[0,1,2]"), k=4)
solution(stringToListNode("[0,1,2]"), k=0)
solution(stringToListNode("[]"), k=1)
solution(stringToListNode("[1]"), k=1)
