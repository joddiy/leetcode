from utils.tools import *


def solution(head):
    _head = ListNode(None)
    while head:
        tmp = ListNode(head.val)
        _head.next, tmp.next = tmp, _head.next
        head = head.next
    return _head.next


def solution(head):
    if not head:
        return None

    def recursive(head):
        tmp = ListNode(head.val)
        if not head.next:
            return tmp, tmp
        else:
            _head, _tail = recursive(head.next)
            _tail.next = tmp
            return _head, tmp

    _head, _ = recursive(head)
    return _head


print(listNodeToString(solution(stringToListNode("[1,2,3,4,5]"))))
print(listNodeToString(solution(stringToListNode("[]"))))