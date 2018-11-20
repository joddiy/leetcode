# -*- coding: utf-8 -*-
# file: reverseList.py
# author: joddiyzhang@gmail.com
# time: 2018/11/20 8:01 PM
# ------------------------------------------------------------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     new_tail = None
    #     cur_node = head
    #     while cur_node is not None:
    #         tmp_node = ListNode(cur_node.val)
    #         tmp_node.next = new_tail
    #         new_tail = tmp_node
    #         cur_node = cur_node.next
    #     return new_tail

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head

        while cur:
            next_p = cur.next
            cur.next = prev  # each step, add the current node to the head of the previous list
            prev = cur
            cur = next_p

        return prev
