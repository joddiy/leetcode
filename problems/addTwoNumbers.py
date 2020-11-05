from tools import *


@print_
@list_node
def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carry = 0
    res = ListNode(None)
    res_ = res
    while l1 or l2 or carry:
        sum_ = carry
        if l1:
            sum_ += l1.val
            l1 = l1.next
        if l2:
            sum_ += l2.val
            l2 = l2.next
        res_.next = ListNode(sum_ % 10)
        res_ = res_.next
        carry = sum_ // 10

    return res.next


addTwoNumbers("[2,4,3]", "[5,6,4]")
addTwoNumbers("[0]", "[0]")
addTwoNumbers("[9,9,9,9,9,9,9]", "[9,9,9,9]")