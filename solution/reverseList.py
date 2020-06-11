from utils.tools import *


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_tail = None
        cur_node = head
        while cur_node is not None:
            tmp_node = ListNode(cur_node.val)
            tmp_node.next = new_tail
            new_tail = tmp_node
            cur_node = cur_node.next
        return new_tail

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

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def recursive(head):
            if head.next:
                new_head, tail = recursive(head.next)
                tail.next = head
                return new_head, head
            else:
                return head, head

        if not head or not head.next:
            return head
        new_head, tail = recursive(head)
        tail.next = None
        return new_head


print(listNodeToString(Solution().reverseList(
    stringToListNode("[1,2,3,4,5]"))))
