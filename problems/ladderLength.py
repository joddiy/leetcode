from tools import *


class Solution(object):
    @print_
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        tmp_b = set(beginWord)
        tmp_e = set(endWord)
        min_ = len(endWord)
        min_dex = None
        for idx, w in enumerate(wordList):
            tmp_w = set(w)
            if len(tmp_w - tmp_b) == 1 and len(tmp_w - tmp_e)<:
                min_ = min(min_, )
            print()
            break



solution = Solution().ladderLength

solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
