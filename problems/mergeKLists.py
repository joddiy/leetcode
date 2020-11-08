from tools import *
from heapq import *

@print_
@list_node
def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    ret = ListNode(None)
    head = ret
    heap_ = []
    for i in lists:
        if i:
            heap_.append((i.val, i))
    heapify(heap_)
    while heap_:
        _, node = heappop(heap_)
        if node.next:
            tmp_ = node.next
            heappush(heap_, (tmp_.val, tmp_))
        ret.next = node
        ret = ret.next
    return head.next


mergeKLists([
    stringToListNode("[1,4,5]"),
    stringToListNode("[1,3,4]"),
    stringToListNode("[2,6]"),
])
mergeKLists([
    stringToListNode("[]")
])
mergeKLists([])
