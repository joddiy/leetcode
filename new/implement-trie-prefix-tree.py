import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Trie(object):

    def __init__(self):
        self.tree = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        tmp_tree = self.tree
        for idx, ch in enumerate(word):
            if ch not in tmp_tree:
                tmp_tree[ch] = {}
            tmp_tree = tmp_tree[ch]
        tmp_tree["exist"] = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        tmp_tree = self.tree
        for ch in word:
            if ch not in tmp_tree:
                return False
            else:
                tmp_tree = tmp_tree[ch]
        return tmp_tree.get("exist", False)

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        tmp_tree = self.tree
        for ch in prefix:
            if ch not in tmp_tree:
                return False
            else:
                tmp_tree = tmp_tree[ch]
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # return True
print(trie.search("app"))  # return False
print(trie.startsWith("app"))  # return True
print(trie.startsWith("appb"))  # return False
print(trie.startsWith("apple"))  # return True
trie.insert("app")
print(trie.search("app"))  # return True
