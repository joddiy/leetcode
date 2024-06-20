import sys

from tools import *
import pprint
from collections import Counter


class Solution(object):
    @print_
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count_ = Counter(magazine)
        for c in ransomNote:
            count_[c] -= 1
            if count_[c] < 0:
                return False
        return True


solution = Solution().canConstruct
solution(ransomNote="a", magazine="b")
solution(ransomNote="aa", magazine="ab")
solution(ransomNote="aa", magazine="aab")
