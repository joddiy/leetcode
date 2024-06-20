import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Trie(object):

    def __init__(self):
        self.store = defaultdict(Trie)
        self.word = False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        t = self
        for w in word:
            t = t.store[w]
        t.word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        t = self
        for w in word:
            if w not in t.store:
                return False
            else:
                t = t.store[w]
        return t.word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        t = self
        for w in prefix:
            if w not in t.store:
                return False
            else:
                t = t.store[w]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))
