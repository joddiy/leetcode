import math
import sys

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
        map_ = {}
        def create(node):
            if not node:
                return node
            elif id(node) not in map_:
                new_node = Node(node.val)
                map_[id(node)] = new_node
                new_node.next = create(node.next)
                new_node.random = create(node.random)
                return map_[id(node)]

        new_head = create(head)
        return new_head


solution = Solution().copyRandomList
