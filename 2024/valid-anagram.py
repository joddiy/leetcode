import sys

from tools import *
import pprint
from collections import Counter


class Solution(object):
    @print_
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t = Counter(t)
        for c in s:
            if c in t and t[c] > 0:
                t[c] -= 1
            else:
                return False
        return sum(t.values()) == 0


solution = Solution().isAnagram
solution(s="anagram", t="nagaram")
solution(s="rat", t="car")
solution(s="a", t="ab")
