from tools import *
import heapq


class Solution(object):
    @print_
    @list_node
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ret = ListNode(None)
        head = ret
        heap_ = [(l.val, l) for l in lists if l]
        heapq.heapify(heap_)
        while heap_:
            _, node = heapq.heappop(heap_)
            head.next = node
            if node.next:
                heapq.heappush(heap_, (node.next.val, node.next))
            head = head.next
        return ret.next


solutin = Solution().mergeKLists

solutin([
    stringToListNode("[1,4,5]"),
    stringToListNode("[1,3,4]"),
    stringToListNode("[2,6]"),
])
solutin([
    stringToListNode("[1,4,5]"),
    stringToListNode("[1,3,4]"),
    stringToListNode("[]"),
])
solutin([stringToListNode("[]")])
solutin([])
