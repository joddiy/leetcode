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
        cnt_map = {}
        i, j = 0, 0
        max_l = 0
        while j < len(s):
            last_idx = cnt_map.get(s[j], None)
            if last_idx is not None:
                while i <= last_idx:
                    cnt_map.pop(s[i])
                    i += 1
            else:
                cnt_map[s[j]] = j
                j += 1
            max_l = max(max_l, j - i)
        return max_l


solution = Solution().lengthOfLongestSubstring
solution(s="abcabcbb")
solution(s="bbbbb")
solution(s="pwwkew")
