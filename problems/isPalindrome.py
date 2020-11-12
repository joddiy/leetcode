from tools import *


class Solution(object):
    @print_
    @list_node
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # find the start of the second half
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next

        # reverse
        ret = ListNode(None)
        while slow:
            # pick the node
            tmp = slow
            slow = slow.next
            # add from head
            tmp.next = ret.next
            ret.next = tmp

        # compare
        ret = ret.next
        while ret:
            if ret.val != head.val:
                return False
            ret = ret.next
            head = head.next
        return True


solution = Solution().isPalindrome

solution("[1,2,2,1]")
solution("[1,2,1]")
solution("[1,2]")