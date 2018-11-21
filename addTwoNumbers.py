# -*- coding: utf-8 -*-
# file: addTwoNumbers.py
# author: joddiyzhang@gmail.com
# time: 2018/11/20 1:55 PM
# ------------------------------------------------------------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        current_node = res
        carry = 0
        tmp_l1 = l1
        tmp_l2 = l2
        # init
        if tmp_l1 is not None:
            current_node.val += tmp_l1.val
            tmp_l1 = tmp_l1.next
        if tmp_l2 is not None:
            current_node.val += tmp_l2.val
            tmp_l2 = tmp_l2.next
        if current_node.val >= 10:
            current_node.val -= 10
            carry = 1
        else:
            carry = 0
        # next
        while tmp_l1 is not None or tmp_l2 is not None or carry != 0:
            current_node.next = ListNode(0)
            current_node = current_node.next
            if tmp_l1 is not None:
                current_node.val += tmp_l1.val
                tmp_l1 = tmp_l1.next
            if tmp_l2 is not None:
                current_node.val += tmp_l2.val
                tmp_l2 = tmp_l2.next
            current_node.val += carry
            if current_node.val >= 10:
                current_node.val -= 10
                carry = 1
            else:
                carry = 0
        return res


print(Solution().addTwoNumbers([2, 4, 3], [5, 6, 4]))
