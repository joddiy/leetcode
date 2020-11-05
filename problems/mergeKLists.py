from utils.tools import *
from heapq import *


def solution(lists):
    hp = []
    heapify(hp)
    head = ListNode(None)
    p = head
    for l in lists:
        heappush(hp, l)
    while hp:
        node = heappop(hp)
        p.next = node
        p = p.next
        if node.next:
            heappush(hp, node.next)

    return head.next


print(
    listNodeToString(
        solution([
            stringToListNode("[1,4,5]"),
            stringToListNode("[1,3,4]"),
            stringToListNode("[2,6]"),
        ])))
