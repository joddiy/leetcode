import heapq
import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap_ = []
        heapq.heapify(heap_)
        for head in lists:
            if head:
                heapq.heappush(heap_, [head.val, head])

        ret = ListNode(None)
        p = ret
        while heap_:
            val, node = heapq.heappop(heap_)
            next_node = node.next
            if next_node:
                heapq.heappush(heap_, [next_node.val, next_node])
            p.next = node
            node.next = None
            p = p.next

        return ret.next


solution = Solution().mergeKLists
solution([stringToListNode(x) for x in ["[1,4,5]", "[1,3,4]", "[2,6]"]])
solution([stringToListNode(x) for x in []])
# solution([stringToListNode(x) for x in [""]])
