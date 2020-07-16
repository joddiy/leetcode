from utils.tools import *


def solution(head, val):
    if not head:
        return head
    new_head = ListNode(None)
    new_head.next = head
    p = new_head

    while p.next and p.next.next:
        if p.next.val == val:
            p.next = p.next.next
        else:
            p = p.next
    if p.next and p.next.val == val:
        p.next = None
    return new_head.next


# print(listNodeToString(solution(stringToListNode("[1,2,3,4,5]"), 3)))
# print(listNodeToString(solution(stringToListNode("[1,2,3,4,5]"), 1)))
# print(listNodeToString(solution(stringToListNode("[1,2,3,4,5]"), 5)))
print(listNodeToString(solution(stringToListNode("[1,1,1,4,5]"), 1)))
print(listNodeToString(solution(stringToListNode("[1,1]"), 1)))
# print(listNodeToString(solution(stringToListNode("[1,2,3,4,5]"), 2)))