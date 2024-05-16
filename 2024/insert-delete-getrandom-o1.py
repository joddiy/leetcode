import random
import sys

from tools import *
import pprint
import random


class RandomizedSet(object):

    def __init__(self):
        self.points = {}
        self.values = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.points:
            return False
        else:
            self.points[val] = len(self.values)
            self.values.append(val)
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.points:
            last_val = self.values[-1]
            val_pos, last_pos = self.points[val], self.points[last_val]
            self.values[val_pos], self.values[last_pos] = self.values[last_pos], self.values[val_pos]
            self.points[val], self.points[last_val] = last_pos, val_pos
            self.values.pop(-1)
            del self.points[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        random_idx = random.randint(0, len(self.values) - 1)
        return self.values[random_idx]


obj = RandomizedSet()
print(obj.insert(0))
print(obj.insert(1))
print(obj.remove(0))
print(obj.insert(2))
print(obj.remove(1))
print(obj.getRandom())
