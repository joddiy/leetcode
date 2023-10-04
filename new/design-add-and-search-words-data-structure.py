import math
import pprint
import sys

from tools import *
from collections import defaultdict


class WordDictionary(object):

    def __init__(self):
        self.tree = {}

    def addWord(self, word):
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
        n = len(word)

        def recursive(tmp_tree, i):
            if i < n:
                w = word[i]
                if w == ".":
                    for k in tmp_tree.keys():
                        if k == "exist":
                            continue
                        if recursive(tmp_tree[k], i + 1):
                            return True
                    return False
                elif w not in tmp_tree:
                    return False
                else:
                    return recursive(tmp_tree[w], i + 1)
            else:
                return tmp_tree.get("exist", False)

        return recursive(self.tree, 0)


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
# wordDictionary.addWord("bad")
# wordDictionary.addWord("dad")
# wordDictionary.addWord("mad")
# print(wordDictionary.search("pad"))  # return False
# print(wordDictionary.search("bad"))  # return True
# print(wordDictionary.search(".ad"))  # return True
# print(wordDictionary.search("b.."))  # return True
wordDictionary.addWord("a")
wordDictionary.addWord("a")
# print(wordDictionary.search("."))
# print(wordDictionary.search("a"))
# print(wordDictionary.search("aa"))
# print(wordDictionary.search("a"))
# print(wordDictionary.search(".a"))
print(wordDictionary.search("a."))
