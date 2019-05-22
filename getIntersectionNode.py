from utils.tools import stringToListNode, ListNode


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        

head_a = stringToListNode('[4,1]')
head_b = stringToListNode('[5,0,1]')
head_c = stringToListNode('[8,4,5]')
head_a.next.next = head_c
head_a.next.next.next = head_c

Solution().getIntersectionNode(head_a, head_b)

