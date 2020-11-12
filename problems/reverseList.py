from tools import *


class Solution(object):
    @print_
    @list_node
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret = ListNode(None)
        while head:
            # pick the node
            tmp = head
            head = head.next
            # add from head
            tmp.next = ret.next
            ret.next = tmp
        return ret.next


solution = Solution().reverseList

solution("[1,2,3,4,5]")
solution("[]")