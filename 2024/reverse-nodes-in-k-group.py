import math
import sys

from tools import *
import pprint
from collections import defaultdict
import heapq


class Solution(object):
    @print_
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        ret = ListNode(None)
        p, q = ret, ret
        i = 0
        m = 0
        tmp_head = head
        while tmp_head:
            m += 1
            tmp_head = tmp_head.next
        m_ = (m // k) * k

        def insert_from_head(tmp_head, tmp_node):
            tmp_next_node = tmp_node.next
            tmp_node.next = tmp_head.next
            tmp_head.next = tmp_node
            return tmp_next_node

        while head and i < m_:
            # record the first insert node as the tail(the next head)
            if i % k == 0:
                p = q
                q = head
                head = insert_from_head(p, head)
            else:
                head = insert_from_head(p, head)
            i += 1

        q.next = head
        return ret.next



solution = Solution().reverseKGroup
solution(head=stringToListNode("[1,2,3,4,5]"), k=3)
