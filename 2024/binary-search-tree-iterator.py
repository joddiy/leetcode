import math
import sys

from tools import *
import pprint
from collections import defaultdict


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        if root:
            self.stack.append(root)
        self._push_left()

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        if node.right:
            self.stack.append(node.right)
            self._push_left()
        return node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0

    def _push_left(self):
        if self.stack:
            while self.stack[-1].left:
                self.stack.append(self.stack[-1].left)


# Your BSTIterator object will be instantiated and called as such:
obj = BSTIterator(stringToTreeNode("[7,3,15,null,null,9,20]"))
param_1 = obj.next()
param_2 = obj.hasNext()
