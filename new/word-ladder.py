import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        res = 1
        s1 = {beginWord}
        s2 = {endWord}
        while s1 and s2:
            if len(s2) < len(s1):
                s1, s2 = s2, s1
            next_s1 = set()
            for word in s1:
                for i in range(len(word)):
                    for char in chars:
                        candidate = word[:i] + char + word[i + 1:]
                        if candidate in s2:
                            return res + 1
                        if candidate not in wordSet:
                            continue
                        wordSet.remove(candidate)
                        next_s1.add(candidate)
            s1 = next_s1
            res += 1
        return 0


solution = Solution().ladderLength
solution(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"])
solution(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"])
