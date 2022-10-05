from tools import *

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    @print_
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        ret = root
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next
        return ret

solution = Solution().connect

solution("[1, 2, 3, 4, 5, 6, 7]")
