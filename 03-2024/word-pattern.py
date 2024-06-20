import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False
        map_ = {}
        set_ = set()
        for i in range(len(pattern)):
            p, w = pattern[i], words[i]
            if p not in map_:
                map_[p] = w
                if w in set_:
                    return False
                set_.add(w)
            elif map_[p] != w:
                return False
        return True


solution = Solution().wordPattern
solution(pattern="abba", s="dog cat cat dog")
solution(pattern="abba", s="dog cat cat fish")
solution(pattern="aaaa", s="dog cat cat dog")
solution(pattern="ab", s="dog dog")
