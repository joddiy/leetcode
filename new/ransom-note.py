import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count_map = defaultdict(int)
        for c in magazine:
            count_map[c] += 1
        for c in ransomNote:
            count_map[c] -= 1
        for v in count_map.values():
            if v < 0:
                return False
        return True


solution = Solution().canConstruct
solution(ransomNote="a", magazine="b")
solution(ransomNote="aa", magazine="ab")
solution(ransomNote="aa", magazine="aab")
