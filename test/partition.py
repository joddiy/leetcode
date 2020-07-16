from utils.tools import *


def solution(head, val):
    less_head = ListNode(None)
    larger_head = ListNode(None)
    p, q = less_head, larger_head
    while head:
        if head.val < val:
            p.next = head
            p = p.next
        else:
            q.next = head
            q = q.next
        head = head.next
        p.next = None
        q.next = None
    p.next = larger_head.next
    return less_head.next


print(listNodeToString(solution(stringToListNode("[1,4,3,2,5,2]"), 3)))
print(listNodeToString(solution(stringToListNode("[3]"), 3)))