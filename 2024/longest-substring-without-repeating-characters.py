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


solution = Solution().lengthOfLongestSubstring
solution(s="abcabcbb")
solution(s="bbbbb")
solution(s="pwwkew")
