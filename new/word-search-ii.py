import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

    def addWord(self, word):
        cur = self
        for ch in word:
            cur = cur.children[ch]
        cur.isWord = True


class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        for word in words:
            root.addWord(word)

        m, n = len(board), len(board[0])
        res = set()

        def dfs(i, j, node=root, word=""):
            if i < 0 or i == m or j < 0 or j == n or board[i][j] not in node.children:
                return
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.isWord:
                res.add(word)

            board[i][j] = '#'
            dfs(i + 1, j, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i, j - 1, node, word)
            board[i][j] = word[-1]

        for i in range(m):
            for j in range(n):
                dfs(i, j)
        return list(res)


solution = Solution().findWords
solution(board=[
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"]
], words=["oath", "pea", "eat", "rain"])
