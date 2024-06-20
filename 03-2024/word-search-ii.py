import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

    def add_word(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True


class Solution:
    @print_
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        for word in words:
            root.add_word(word)

        m, n = len(board), len(board[0])
        pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ret = set()

        def find(prefix, i, j, node):
            c = board[i][j]
            if c in node.children:
                child = node.children[c]
                prefix += c
                if child.is_word:
                    ret.add(prefix)

                board[i][j] = '#'
                for x, y in pos:
                    if 0 <= x + i < m and 0 <= y + j < n:
                        find(prefix, x + i, y + j, node.children[c])
                board[i][j] = c

        for i in range(m):
            for j in range(n):
                find("", i, j, root)

        return list(ret)


solution = Solution().findWords
solution(board=[
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"]
], words=["oath", "pea", "eat", "rain"])
solution(board=[["a", "b"], ["c", "d"]], words=["abcb"])
solution(board=[["a"]], words=["a"])
