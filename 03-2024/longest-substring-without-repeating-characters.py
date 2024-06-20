import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        i, j = 0, 0
        map_ = {s[0]: 0}
        ret = 1
        while i < n and j < n:
            j += 1
            if j >= n:
                break
            elif s[j] in map_:
                for k in range(i, map_[s[j]]):
                    map_.pop(s[k])
                i = map_[s[j]] + 1
            map_[s[j]] = j
            ret = max(ret, j - i + 1)

        return ret


solution = Solution().lengthOfLongestSubstring
# solution(s="abcabcbb")
# solution(s="bbbbb")
# solution(s="pwwkew")
# solution(s="")
solution(s="abba")
