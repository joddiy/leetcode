import math
import sys

from tools import *
import pprint
from collections import defaultdict


class WordDictionary(object):

    def __init__(self):
        self.map_ = {}

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        map_ = self.map_
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

        def dfs(i, m):
            if i == len(word):
                return 'store' in m
            else:
                w_ = word[i]
                if w_ != '.':
                    if w_ in m:
                        return dfs(i + 1, m[w_])
                    else:
                        return False
                else:
                    for w_ in m.keys():
                        if w_ != 'store' and dfs(i + 1, m[w_]):
                            return True
                    return False

        return dfs(0, self.map_)


# Your Trie object will be instantiated and called as such:
obj = WordDictionary()
# obj.addWord("bad")
# obj.addWord("dad")
# obj.addWord("mad")
# print(obj.search("pad"))
# print(obj.search("bad"))
# print(obj.search(".ad"))
# print(obj.search("b.."))

# obj.addWord("at")
# obj.addWord("and")
# obj.addWord("an")
# obj.addWord("add")
# print(obj.search("a"))
# print(obj.search(".at"))
# obj.addWord("bat")
# print(obj.search(".at"))

obj.addWord("a")
obj.addWord("a")
print(obj.search("."))
print(obj.search("aa"))
print(obj.search(".a"))
print(obj.search("a."))
