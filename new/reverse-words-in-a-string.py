import pprint

from tools import *


class Solution(object):
    @print_
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # solution 1
        # return " ".join(s.split()[::-1])

        # solution 2
        return " ".join(x[::-1] for x in s[::-1].split())


solution = Solution().reverseWords
solution("the sky is blue")
solution("a good   example")
solution("  hello world  ")
