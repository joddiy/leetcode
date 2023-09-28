from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        char_map = defaultdict(int)
        for c in s:
            char_map[c] += 1
        for c in t:
            char_map[c] -= 1
            if char_map[c] < 0:
                return False
        return True


solution = Solution().isAnagram
solution(s="anagram", t="nagaram")
solution(s="rat", t="car")
