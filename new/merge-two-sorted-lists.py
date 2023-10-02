import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(None)
        p = head
        while list1 or list2:
            if list1 is None:
                p.next = list2
                break
            if list2 is None:
                p.next = list1
                break
            if list1.val <= list2.val:
                p.next = ListNode(list1.val)
                list1 = list1.next
            else:
                p.next = ListNode(list2.val)
                list2 = list2.next
            p = p.next
        return head.next


solution = Solution().mergeTwoLists
solution(list1=stringToListNode("[1,2,4]"), list2=stringToListNode("[1,3,4]"))
solution(list1=stringToListNode("[]"), list2=stringToListNode("[0]"))
