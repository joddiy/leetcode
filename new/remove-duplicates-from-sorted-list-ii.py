import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        r = ListNode(None)
        r.next = head
        p = r
        pre_v = -101
        # p.next is the node needed to be handled
        while p.next:
            t = p.next
            if t and t.next and t.val == t.next.val:
                p.next = t.next
                pre_v = t.val
            elif t.val == pre_v:
                p.next = t.next
            else:
                p = p.next
        return r.next

solution = Solution().deleteDuplicates
solution(head=stringToListNode("[1,2,3,3,4,4,5]"))
solution(head=stringToListNode("[1,1,1,2,3]"))
solution(head=stringToListNode("[]"))
