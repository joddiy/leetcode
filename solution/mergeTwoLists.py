# -*- coding: utf-8 -*-
# file: mergeTwoLists.py
# author: joddiyzhang@gmail.com
# time: 2018/11/21 12:08 PM
# ------------------------------------------------------------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        elif l2 is None:
            return l1
        elif l1 is None:
            return l2

        if l1.val > l2.val:
            head = ListNode(l2.val)
        else:
            head = ListNode(l1.val)
        head_list = head

        while l1 or l2:
            if not l1:
                head_list.next = l2
            if not l2:
                head_list.next = l1
            if l1.val > l2.val:
                head_list.next = ListNode(l1.val)
                head_list = head_list.next
                l1 = l1.next
            else:
                head_list.next = ListNode(l1.val)
                head_list = head_list.next
                l2 = l2.next
