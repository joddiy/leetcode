from utils.tools import *


def solution(head):
    if not head:
        return head
    new_head = ListNode(None)
    new_head.next = head
    p = new_head
    while p.next and p.next.next:
        i = p.next
        j = i.next
        k = j.next
        p.next = j
        j.next = i
        i.next = k
        p = i

    return new_head.next

def solution(head):
    if not head or not head.next:
        return head
    n = head.next
    head.next = solution(head.next.next)
    n.next = head
    return n


print(listNodeToString(solution(stringToListNode("[1,2,3,4]"))))
print(listNodeToString(solution(stringToListNode("[1,2,3,4,5]"))))