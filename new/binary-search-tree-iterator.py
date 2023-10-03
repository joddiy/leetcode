import math
import pprint
import sys

from tools import *
from collections import defaultdict


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        if root:
            self.stack.append(root)
        self.pushLeft()

    @print_
    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        if node.right:
            self.stack.append(node.right)
            self.pushLeft()
        return node.val

    @print_
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def pushLeft(self):
        if self.stack:
            while self.stack[-1].left:
                self.stack.append(self.stack[-1].left)


bSTIterator = BSTIterator(stringToTreeNode("[7, 3, 15, null, null, 9, 20]"))
bSTIterator.next()  # return 3
bSTIterator.next()  # return 7
bSTIterator.hasNext()  # return True
bSTIterator.next()  # return 9
bSTIterator.hasNext()  # return True
bSTIterator.next()  # return 15
bSTIterator.hasNext()  # return True
bSTIterator.next()  # return 20
bSTIterator.hasNext()  # return False
