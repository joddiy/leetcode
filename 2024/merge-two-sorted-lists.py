import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ret = ListNode(None)
        p = ret
        while list1 or list2:
            if list1 and list2:
                if list1.val > list2.val:
                    p.next = list2
                    list2 = list2.next
                    p.next.next = None
                else:
                    p.next = list1
                    list1 = list1.next
                    p.next.next = None
            elif list1:
                p.next = list1
                list1 = list1.next
                p.next.next = None
            else:
                p.next = list2
                list2 = list2.next
                p.next.next = None
            p = p.next
        return ret.next

solution = Solution().mergeTwoLists
solution(list1=stringToListNode("[1,2,4]"), list2=stringToListNode("[1,3,4]"))
solution(list1=stringToListNode("[]"), list2=stringToListNode("[]"))
