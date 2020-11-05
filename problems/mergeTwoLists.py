from tools import *


@print_
@list_node
def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    ret = ListNode(None)
    head = ret
    while l1 and l2:
        if l1.val <= l2.val:
            ret.next = l1
            l1 = l1.next
        else:
            ret.next = l2
            l2 = l2.next
        ret = ret.next
        ret.next = None
    if l1:
        ret.next = l1
    if l2:
        ret.next = l2
    return head.next



mergeTwoLists("[1,2,4]", "[1,3,4]")
mergeTwoLists("[]", "[]")
mergeTwoLists("[]", "[0]")