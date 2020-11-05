from utils.tools import *


def solution(head):
    rev = ListNode(None)
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        _slow = slow
        slow = slow.next
        _slow.next = rev.next
        rev.next = _slow
    if fast:
        slow = slow.next
    rev = rev.next
    while rev and slow:
        if rev.val != slow.val:
            return False
        rev = rev.next
        slow = slow.next
    return True


print(solution(stringToListNode("[1,2,2,1]")))
print(solution(stringToListNode("[1,2,1]")))
print(solution(stringToListNode("[1,2]")))