from utils.tools import *

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = []
        for l in lists:
            if l:
                heapq.heappush(q, (l.val, l))
        while q:
            val, node = heapq.heappop(q)
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                heapq.heappush(q, (node.val, node))
        return head.next

Solution().mergeKLists([stringToListNode('[1,4,5]'), stringToListNode(
    '[1,3,4]'), stringToListNode('[2,6]')])
