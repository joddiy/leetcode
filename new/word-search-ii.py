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
        ret = set()

        def dfs(i, j, node, prefix):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] not in node.children:
                return

            node = node.children[board[i][j]]
            prefix += board[i][j]
            if node.is_word:
                ret.add(prefix)

            board[i][j] = '#'
            dfs(i - 1, j, node, prefix)
            dfs(i + 1, j, node, prefix)
            dfs(i, j - 1, node, prefix)
            dfs(i, j + 1, node, prefix)
            board[i][j] = prefix[-1]
            return

        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")

        return list(ret)


solution = Solution().findWords
solution(board=[
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"]
], words=["oath", "pea", "eat", "rain"])
solution(board=[["a", "b"], ["c", "d"]], words=["abcb"])
