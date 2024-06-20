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
        head_ = []
        heapq.heapify(head_)
        for head in lists:
            if head:
                heapq.heappush(head_, [head.val, head])

        ret = ListNode(None)
        p = ret
        while head_:
            val, node = heapq.heappop(head_)
            if node.next:
                heapq.heappush(head_, [node.next.val, node.next])
            node.next = None
            p.next = node
            p = p.next
        return ret.next


solution = Solution().mergeKLists
solution([stringToListNode(x) for x in ["[1,4,5]", "[1,3,4]", "[2,6]"]])
solution([stringToListNode(x) for x in []])
solution([])
