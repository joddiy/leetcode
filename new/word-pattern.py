from tools import *
import pprint
from collections import  defaultdict


class Solution(object):
    @print_
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern_map = defaultdict(str)
        word_map = defaultdict(str)
        ss = s.split()
        if len(ss) != len(pattern):
            return False
        for i in range(len(ss)):
            p, w = pattern[i], ss[i]
            if p not in pattern_map and w not in word_map:
                pattern_map[p] = w
                word_map[w] = p
            elif pattern_map[p] != w or word_map[w] != p:
                return False
        return True


solution = Solution().wordPattern
solution(pattern="abba", s="dog cat cat dog")
solution(pattern="aaaa", s="dog cat cat dog")
solution(pattern="abba", s="dog dog dog dog")
