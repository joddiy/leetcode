import heapq
import pprint
from tools import *
from collections import defaultdict


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []  # max heap
        self.right = []  # min heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.left) == len(self.right):
            heapq.heappush(self.left, -heapq.heappushpop(self.right, num))
        else:
            heapq.heappush(self.right, -heapq.heappushpop(self.left, -num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left) == len(self.right):
            return float(-self.left[0] + self.right[0]) / 2.
        else:
            return float(-self.left[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
