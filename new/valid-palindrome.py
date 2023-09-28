from tools import *
import pprint


class Solution(object):
    @print_
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        valid_c = set([ord('a') + x for x in range(26)] + [ord('0') + x for x in range(10)])
        ss = ""
        for c in s:
            if ord(c) in valid_c:
                ss += c
        return ss == ss[::-1]


solution = Solution().isPalindrome
solution(s="A man, a plan, a canal: Panama")
