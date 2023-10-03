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
        self.node_map = {}
        self.connected = set()

        def build(node):
            if node.val in self.node_map:
                return
            else:
                self.node_map[node.val] = Node(node.val)
                for neighbor in node.neighbors:
                    build(neighbor)

        def connect(node):
            if node.val in self.connected:
                return
            else:
                root_ = self.node_map[node.val]
                self.connected.add(root_.val)
                for neighbor in node.neighbors:
                    root_.neighbors.append(self.node_map[neighbor.val])
                    connect(neighbor)

        if not node:
            return None
        else:
            build(node)
            connect(node)
            return self.node_map[node.val]


solution = Solution().cloneGraph
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]
solution(node1)
