from utils.tools import *


# O(n)
def solution(head, n):
    t = ListNode(None)
    t.next = head
    p = t
    q = t
    for _ in range(n):
        p = p.next
    while p.next:
        q = q.next
        p = p.next
    q.next = q.next.next
    return t.next


print(listNodeToString(solution(stringToListNode("[1,2,3,4,5]"), 2)))
# print(listNodeToString(solution(stringToListNode("[1]"), 1)))
