import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        p = head
        carry = 0
        while l1 or l2:
            v_l1, v_l2 = 0, 0
            if l1:
                v_l1 = l1.val
                l1 = l1.next
            if l2:
                v_l2 = l2.val
                l2 = l2.next
            val = v_l1 + v_l2 + carry
            p.next = ListNode(val % 10)
            carry = val // 10
            p = p.next
        if carry:
            p.next = ListNode(carry)
        return head.next


solution = Solution().addTwoNumbers
solution(l1=stringToListNode("[2,4,3]"), l2=stringToListNode("[5,6,4]"))
solution(l1=stringToListNode("[0]"), l2=stringToListNode("[0]"))
solution(l1=stringToListNode("[0,1]"), l2=stringToListNode("[1]"))
solution(l1=stringToListNode("[9,9,9,9,9,9,9]"), l2=stringToListNode("[9,9,9,9]"))
