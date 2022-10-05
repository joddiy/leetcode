from tools import *


class Solution(object):
    # O(nlogn) merge sort
    @print_
    @list_node
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def split(head):
            ret = ListNode(None)
            ret.next = head
            slow = fast = ret
            slow_pre = None
            while fast and fast.next:
                slow_pre = slow
                slow = slow.next
                fast = fast.next.next
            if fast:
                slow_pre = slow
                slow = slow.next
            if slow_pre:
                slow_pre.next = None

            return ret.next, slow

        def sort(head):
            if not head or not head.next:
                return head
            left, right = split(head)
            left = sort(left)
            right = sort(right)
            # merge
            ret = ListNode(None)
            head_ = ret
            while left or right:
                if left and right:
                    if left.val <= right.val:
                        ret.next = left
                        left = left.next
                    else:
                        ret.next = right
                        right = right.next
                elif left:
                    ret.next = left
                    left = left.next
                else:
                    ret.next = right
                    right = right.next
                ret = ret.next

            return head_.next

        return sort(head)

        # return sort(head)[0]

    # O(n^2) for worst-case, quick sort
    # @print_
    # @list_node
    # def sortList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     def sort(head):
    #         if not head:
    #             return None, None

    #         mid_list = ListNode(None)
    #         left_list = ListNode(None)
    #         right_list = ListNode(None)

    #         _m = mid_list
    #         _l = left_list
    #         _r = right_list

    #         m = head.val
    #         while head:
    #             if head.val < m:
    #                 _l.next = head
    #                 _l = _l.next
    #                 head = head.next
    #                 _l.next = None
    #             elif head.val > m:
    #                 _r.next = head
    #                 _r = _r.next
    #                 head = head.next
    #                 _r.next = None
    #             else:
    #                 _m.next = head
    #                 _m = _m.next
    #                 head = head.next
    #                 _m.next = None

    #         ret_h = mid_list.next
    #         ret_t = _m

    #         # recursive
    #         l_h, l_t = sort(left_list.next)
    #         r_h, r_t = sort(right_list.next)

    #         # concate
    #         if l_t:
    #             l_t.next = ret_h
    #             ret_h = l_h

    #         if r_h:
    #             ret_t.next = r_h
    #             ret_t = r_t

    #         return ret_h, ret_t

    #     return sort(head)[0]


solution = Solution().sortList

solution("[4,2,1,3,5]")
solution("[4,2,1,3]")
solution("[4]")
solution("[4,2]")
solution("[-1,5,3,4,0]")
solution("[]")
solution("[-1]")