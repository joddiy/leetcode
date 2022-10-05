# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

#

# class NestedIterator(object):
#     def __init__(self, nestedList):
#         """
#         Initialize your data structure here.
#         :type nestedList: List[NestedInteger]
#         """
#         self.items = nestedList

#     def next(self):
#         """
#         :rtype: int
#         """
#         for x in self.items:
#             if isinstance(x, list):
#                 yield from NestedIterator(x).next()
#             else:
#                 yield x

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator([1, [4, [6]]]), []
# for t in i.next():
#     v.append(t)


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False


# Your NestedIterator object will be instantiated and called as such:
i, v = NestedIterator([1, [4, [6]]]), []
while i.hasNext():
    print(v)
    v.append(i.next())

print(v)