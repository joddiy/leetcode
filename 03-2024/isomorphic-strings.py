import sys

from tools import *
import pprint
from collections import Counter


class Solution(object):
    @print_
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_ = {}
        set_ = set()
        for i in range(len(s)):
            if s[i] not in map_:
                map_[s[i]] = t[i]
                if t[i] in set_:
                    return False
                set_.add(t[i])
            elif map_[s[i]] != t[i]:
                return False
        return True


solution = Solution().isIsomorphic
# solution(s="egg", t="add")
# solution(s="foo", t="bar")
# solution(s="paper", t="title")
solution(s="badc", t="baba")
