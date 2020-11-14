from tools import *
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

        d = defaultdict(int)
        for c in s:
            d[c] += 1

        for c in t:
            d[c] -= 1
            if d[c] < 0:
                return False

        return True


solution = Solution().isAnagram
solution(s="anagram", t="nagaram")
