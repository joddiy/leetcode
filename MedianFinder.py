# insertion sort
from heapq import *


def binary_search(arr, val, start, end):
    # we need to distinugish whether we should insert
    # before or after the left boundary.
    # imagine [0] is the last step of the binary search
    # and we need to decide where to insert -1
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1

    # this occurs if we are moving beyond left\'s boundary
    # meaning the left boundary is the least position to
    # find a number greater than val
    if start > end:
        return start

    mid = (start+end)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.output = []

    def addNum(self, num):
            """
            :type num: int
            :rtype: None
            """

            if len(self.output) == 0:
                self.output.append(num)
            else:
                j = binary_search(self.output, num, 0, len(self.output)-1)
                print(j)
                self.output = self.output[0:j] + [num] + self.output[j:]
            print(self.output)

    def findMedian(self):
        """
        :rtype: float
        """
        length = len(self.output)
        if length % 2 == 0:
            return (self.output[length//2] + self.output[length//2-1])/2.
        else:
            return self.output[length//2]

# two heaps


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        small, large = self.heaps
        # small heap stors the biggest value at first
        # large heap stores the smallest value at first
        # push num into large queue
        # pop smallest one from large quque and push into small queue
        heappush(small, -heappushpop(large, num))
        # make sure the large queeu is bigger than small queue
        # for exmaple, if there is only one value, the value will be pushed into large quque finally
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        """
        :rtype: float
        """
        small, large = self.heaps
        # if there are odd number of values, return large[0]
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


class MedianFinder(object):

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(-1)
obj.addNum(-2)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(5)
param_3 = obj.findMedian()
print(param_3)
