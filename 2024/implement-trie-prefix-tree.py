import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Trie(object):

    def __init__(self):
        self.map = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        map_ = self.map
        for i, w in enumerate(word):
            if w not in map_:
                map_[w] = {}
            map_ = map_[w]
            if i == len(word) - 1:
                map_['store'] = 1

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        map_ = self.map
        for i, w in enumerate(word):
            if w not in map_:
                return False
            else:
                map_ = map_[w]
            if i == len(word) - 1:
                return 'store' in map_

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        map_ = self.map
        for i, w in enumerate(prefix):
            if w not in map_:
                return False
            else:
                map_ = map_[w]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))
