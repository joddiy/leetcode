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

        def build(node):
            le = ListNode(None)
            ll = ListNode(None)
            lr = ListNode(None)
            p, le_end, ll_end, lr_end = node, le, ll, lr
            while p:
                p_next = p.next
                if p.val < node.val:
                    ll_end.next = p
                    ll_end = ll_end.next
                elif p.val > node.val:
                    lr_end.next = p
                    lr_end = lr_end.next
                else:
                    le_end.next = p
                    le_end = le_end.next
                p.next = None
                p = p_next

            ret_head, ret_end = None, None
            if ll.next:
                ret_head, ret_end = build(ll.next)
            if le.next:
                if ret_head is not None:
                    ret_end.next = le.next
                    ret_end = le_end
                else:
                    ret_head, ret_end = le, le_end
            if lr.next:
                lr, lr_end = build(lr.next)
                if ret_head is not None:
                    ret_end.next = lr.next
                    ret_end = lr_end
                else:
                    ret_head, ret_end = lr, lr_end
            return ret_head, ret_end

        if not head:
            return head
        ret, _ = build(head)
        return ret.next


solution = Solution().sortList
solution(head=stringToListNode("[4,2,1,3]"))
solution(head=stringToListNode("[-1,5,3,4,0]"))
solution(head=stringToListNode("[]"))
