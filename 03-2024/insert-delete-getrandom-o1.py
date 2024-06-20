import random
import sys

from tools import *
import pprint
import random


class RandomizedSet(object):

    def __init__(self):
        self.point = {}
        self.storage = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.point:
            self.storage.append(val)
            self.point[val] = len(self.storage) - 1
            return True
        else:
            return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.point:
            return False
        else:
            pos = self.point[val]
            last_val = self.storage[-1]
            # replace with the last element
            self.storage[pos] = last_val
            self.point[last_val] = pos
            # clean
            self.point.pop(val)
            self.storage.pop(-1)
            return True

    def getRandom(self):
        """
        :rtype: int
        """
        return self.storage[random.randint(0, len(self.storage) - 1)]


obj = RandomizedSet()
print(obj.insert(0))
print(obj.insert(1))
print(obj.remove(0))
print(obj.insert(2))
print(obj.remove(1))
print(obj.getRandom())
