from tools import *


@print_
@list_node
def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    ret = ListNode(None)
    ret.next = head
    p, q = ret, ret
    for _ in range(n + 1):
        p = p.next
    while p:
        p = p.next
        q = q.next
    q.next = q.next.next
    return ret.next


removeNthFromEnd("[1,2,3,4,5]", 2)
removeNthFromEnd("[1]", 1)
removeNthFromEnd("[1,2]", 1)