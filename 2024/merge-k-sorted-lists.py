import math
import sys

from tools import *
import pprint
from collections import defaultdict
import heapq

class Solution(object):
    @print_
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap_ = []
        heapq.heapify(heap_)
        for node in lists:
            if node:
                heapq.heappush(heap_, [node.val, node])

        ret = ListNode(None)
        p = ret
        while heap_:
            value, node = heapq.heappop(heap_)
            node_next = node.next
            if node_next:
                heapq.heappush(heap_, [node_next.val, node_next])
            node.next = None
            p.next = node
            p = p.next

        return ret.next




solution = Solution().mergeKLists
solution([stringToListNode(x) for x in ["[1,4,5]", "[1,3,4]", "[2,6]"]])
solution([stringToListNode(x) for x in []])
