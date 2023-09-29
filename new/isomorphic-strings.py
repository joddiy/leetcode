from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        char_map = {}
        keys = set()
        for i in range(m):
            if s[i] not in char_map and t[i] not in keys:
                char_map[s[i]] = t[i]
                keys.add(t[i])
            elif s[i] not in char_map and t[i] in keys:
                return False
            elif s[i] in char_map and t[i] not in keys:
                return False
            elif s[i] in char_map and t[i] in keys and char_map[s[i]] != t[i]:
                return False
        return True


solution = Solution().isIsomorphic
# solution(s="egg", t="add")
solution(s="foo", t="bar")
# solution(s="badc", t="baba")
