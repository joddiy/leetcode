from tools import *


class Solution(object):
    @print_
    @list_node
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(None)
        head = ret
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
            if l2:
                carry += l2.val
            head.next = ListNode(carry % 10)
            carry = carry // 10
            head = head.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return ret.next


solution = Solution().addTwoNumbers

solution("[2,4,3]", "[5,6,4]")
solution("[0]", "[0]")
solution("[9,9,9,9,9,9,9]", "[9,9,9,9]")