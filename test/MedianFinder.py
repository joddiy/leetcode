import heapq


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_heap = []
        self.right_heap = []
        heapq.heapify(self.left_heap)  # big heap
        heapq.heapify(self.right_heap)  # small heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.left_heap) == len(self.right_heap):
            heapq.heappush(self.left_heap,
                           -heapq.heappushpop(self.right_heap, num))
        else:
            heapq.heappush(self.right_heap,
                           -heapq.heappushpop(self.left_heap, -num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left_heap) == len(self.right_heap):
            return float(-self.left_heap[0] + self.right_heap[0]) / 2.
        else:
            return float(-self.left_heap[0])


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())