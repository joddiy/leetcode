# -*- coding: utf-8 -*-
# file: addTwoNumbers.py
# author: joddiyzhang@gmail.com
# time: 2018/11/20 1:55 PM
# ------------------------------------------------------------------------

# Definition for singly-linked list.
from utils.tools import ListNode, stringToListNode, listNodeToString


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        cur = head
        carry = 0
        while l1 or l2 or carry != 0:
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            y = x1 + x2 + carry
            carry = y//10
            y = y % 10
            cur.next = ListNode(y)
            cur = cur.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return head.next

    def addTwoNumbers(self, l1, l2):
        head = ListNode(None)
        temp = head
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            temp.next = ListNode(carry % 10)
            temp = temp.next
            carry //= 10
        return head.next


print(listNodeToString(Solution().addTwoNumbers(stringToListNode(
    "[2,4,3]"), stringToListNode("[5,6,4]"))))
print(listNodeToString(Solution().addTwoNumbers(stringToListNode(
    "[5]"), stringToListNode("[5]"))))
