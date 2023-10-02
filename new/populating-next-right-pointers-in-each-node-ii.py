import math
import pprint
from tools import *
from collections import defaultdict


class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        node_array = [[root, 0]]
        while node_array:
            node, level = node_array.pop(0)
            if node.left:
                node_array.append([node.left, level + 1])
            if node.right:
                node_array.append([node.right, level + 1])
            if node_array and level == node_array[0][1]:
                node.next = node_array[0][0]
        return root


solution = Solution().connect
print(solution(stringToTreeNode("[1,2,3,4,5,null,7]")))
# print(treeNodeToString(solution(stringToTreeNode("[]"))))
# print(treeNodeToString(solution(stringToTreeNode("[1,2,null,3,null,4,null,5]"))))
