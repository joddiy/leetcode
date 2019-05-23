from utils.tools import *


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        bla, _ = self.sort(head)
        print(listNodeToString(bla))
        return bla

    def sort(self, head):
            if not head or not head.next:
                return head, head

            partition = head
            partition_head = partition
            left_head = ListNode(0)
            right_head = ListNode(0)
            left_node = left_head
            right_node = right_head
            node = partition

            # 依次添加node去三个链表
            while node.next:
                node = node.next
                if node.val < partition.val:
                    left_node.next = node
                    left_node = node
                elif node.val > partition.val:
                    right_node.next = node
                    right_node = node
                else:
                    partition.next = node
                    partition = node

            partition.next = None
            left_node.next = None
            right_node.next = None

            left_head, left_tail = self.sort(left_head.next)
            right_head, right_tail = self.sort(right_head.next)

            node = left_tail

            # 拼接
            if not node:
                node = partition_head
                left_head = partition_head
            else:
                node.next = partition_head
            partition.next = right_head
            if not right_tail:
                right_tail = partition
            return left_head, right_tail


Solution().sortList(stringToListNode("[-1,0,5,3,4]"))
