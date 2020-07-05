from utils.tools import *


def solution(headA, headB):
    if not headA or not headB:
        return None
    nodeA = headA
    nodeB = headB
    while nodeA is not nodeB:
        if not nodeA and nodeB:
            return None
        if nodeA.next is None:
            nodeA = headB
        else:
            nodeA = nodeA.next
        if nodeB.next is None:
            nodeB = headA
        else:
            nodeB = nodeB.next
    return nodeA


def solution(headA, headB):

    def len(head):
        ret = 0
        while head:
            ret += 1
            head = head.next
        return ret

    lenA, lenB = len(headA), len(headB)
    diff = abs(lenA - lenB)

    if lenA > lenB:
        for _ in range(diff):
            headA = headA.next
    else:
        for _ in range(diff):
            headB = headB.next

    while headA != headB:
        headA = headA.next
        headB = headB.next
    return headA
