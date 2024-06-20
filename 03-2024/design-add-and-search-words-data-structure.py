import math
import sys

from tools import *
import pprint
from collections import defaultdict


class WordDictionary(object):

    def __init__(self):
        self.store = defaultdict(WordDictionary)
        self.word = False

    def addWord(self, word):
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
        n = len(word)

        def find(i, dic):
            if i == n:
                return dic.word
            else:
                w = word[i]
                if w != '.':
                    return find(i + 1, dic.store[w])
                else:
                    for w in dic.store.keys():
                        if find(i + 1, dic.store[w]):
                            return True
                    return False

        return find(0, self)


# Your Trie object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad"))
print(obj.search("bad"))
print(obj.search(".ad"))
print(obj.search("b.."))

# obj.addWord("at")
# obj.addWord("and")
# obj.addWord("an")
# obj.addWord("add")
# print(obj.search("a"))
# print(obj.search(".at"))
# obj.addWord("bat")
# print(obj.search(".at"))

# obj.addWord("a")
# obj.addWord("a")
# print(obj.search("."))
# print(obj.search("aa"))
# print(obj.search(".a"))
# print(obj.search("a."))
