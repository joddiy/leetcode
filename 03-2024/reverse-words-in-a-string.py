import sys

from tools import *
import pprint


class Solution(object):
    @print_
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.strip().split()[::-1])


solution = Solution().reverseWords
solution(s="the sky is blue")
solution(s="  hello world  ")
solution(s="a good   example")
