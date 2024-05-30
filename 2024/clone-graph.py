import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    @print_
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node

        map_ = {}

        def create(node):
            if id(node) not in map_:
                node_ = Node(node.val)
                map_[id(node)] = node_
                for n in node.neighbors:
                    node_.neighbors.append(create(n))
            else:
                node_ = map_[id(node)]
            return node_

        return create(node)


solution = Solution().cloneGraph
