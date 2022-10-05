from tools import *
from collections import Counter


class Solution(object):
    @print_
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)
        for idx, c in enumerate(s):
            if count[c] == 1:
                return idx
        return -1


solution = Solution().firstUniqChar

solution("leetcode")
solution("loveleetcode")