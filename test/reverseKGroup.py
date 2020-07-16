from utils.tools import *


def solution(head, k):
    if not head:
        return head
    new_head = ListNode(None)
    new_head.next = head
    p = new_head

    while p:
        _k = k
        q = p
        while _k > 0:
            q = q.next
            _k -= 1
            if not q:
                return new_head.next
        _k = k - 1
        q = p.next
        new_p = q
        while _k > 0:
            q_next = q.next
            q_next_next = q_next.next
            _p = p.next
            p.next, q_next.next = q_next, p.next
            q.next = q_next_next
            _k -= 1
        p = new_p

    return new_head.next


# print(listNodeToString(solution(stringToListNode("[1,2,3,4]"))))
print(listNodeToString(solution(stringToListNode("[1,2,3,4,5]"), 3)))
print(listNodeToString(solution(stringToListNode("[1,2,3,4,5]"), 2)))