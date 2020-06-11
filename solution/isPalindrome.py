from utils.tools import ListNode, stringToListNode


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            t_slow = slow.next
            slow.next = rev
            rev = slow
            slow = t_slow
        if fast:  # odd
            slow = slow.next
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        return not rev


print(Solution().isPalindrome(stringToListNode("[1,2,2,1]")))
