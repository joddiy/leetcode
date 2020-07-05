from utils.tools import *

def solution(head):
    if head is None:
        return None

    def recursive(head):
        if head is None:
            return None, None

        partition_node = head
        middle_head = ListNode(None)
        middle_cur = middle_head
        left_head = ListNode(None)
        left_cur = left_head
        right_head = ListNode(None)
        right_cur = right_head

        while head:
            if head.val < partition_node.val:
                left_cur.next = ListNode(head.val)
                left_cur = left_cur.next
            elif head.val > partition_node.val:
                right_cur.next = ListNode(head.val)
                right_cur = right_cur.next
            else:
                middle_cur.next = ListNode(head.val)
                middle_cur = middle_cur.next
            head = head.next
        
        left_head, left_tail = recursive(left_head.next)
        right_head, right_tail = recursive(right_head.next)

        if left_head is not None:
            left_tail.next = middle_head.next
        else:
            left_head = middle_head
        if right_head is not None:
            middle_cur.next = right_head.next
        else:
            right_tail = middle_cur

        return left_head, right_tail

    head, _ = recursive(head)
    return head.next

# print(listNodeToString(solution(stringToListNode("[4,2,1,3]"))))
# print(listNodeToString(solution(stringToListNode("[-1,5,3,4,0]"))))
# print(listNodeToString(solution(stringToListNode("[]"))))
print(listNodeToString(solution(stringToListNode("[-1]"))))