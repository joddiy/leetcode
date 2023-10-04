import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def recursive(node):
            # todo select the pivot from the mid
            less_list = ListNode(None)
            larger_list = ListNode(None)
            p, q = less_list, larger_list
            k = node.next
            node.next = None
            while k:
                k_ = k
                if k.val < node.val:
                    p.next = k
                    p = p.next
                else:
                    q.next = k
                    q = q.next
                k = k.next
                k_.next = None
            start, tail = node, node
            if less_list.next:
                les, let = recursive(less_list.next)
                start = les
                let.next = node
            if larger_list.next:
                las, lat = recursive(larger_list.next)
                node.next = las
                tail = lat
            return start, tail

        s, t = recursive(head)
        return s


solution = Solution().sortList
solution(head=stringToListNode("[4,2,1,3]"))
solution(head=stringToListNode("[-1,5,3,4,0]"))
solution(head=stringToListNode("[-1,5,3,4,0]"))
