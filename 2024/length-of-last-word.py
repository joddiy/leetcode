import sys

from tools import *
import pprint


class Solution(object):
    @print_
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split()[-1])


solution = Solution().lengthOfLastWord
solution(s="Hello World")
solution(s="   fly me   to   the moon  ")
solution(s="luffy is still joyboy")
