from tools import *
import pprint
from collections import defaultdict


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    @print_
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        node_map = defaultdict(Node)
        ret = Node(0)
        p = ret
        q = head
        while q:
            new_ = Node(q.val)
            node_map[q] = new_
            p.next = new_
            p = p.next
            q = q.next

        p = ret.next
        q = head
        while q:
            if q.random is not None:
                p.random = node_map[q.random]
            p = p.next
            q = q.next

        return ret.next


solution = Solution().copyRandomList
solution(head=stringToListNode("[1,2,4]"))
