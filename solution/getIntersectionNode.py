from utils.tools import stringToListNode, ListNode


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p = headA
        q = headB
        if p is None or q is None:
            return None
        while p is not q:
            if not p and not q:
                return None
            if not p:
                p = headB
            else:
                p = p.next
            if not q:
                q = headA
            else:
                q = q.next
        return q

head_a = stringToListNode('[4,1]')
head_b = stringToListNode('[5,0,1]')
head_c = stringToListNode('[8,4,5]')
head_a.next.next = head_c
head_a.next.next.next = head_c

Solution().getIntersectionNode(head_a, head_b)
