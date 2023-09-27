import pprint

from tools import *


class Solution(object):
    @print_
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        reach_word = False
        ret = 0
        for i in range(len(s) - 1, -1, -1):
            if not reach_word and s[i] == " ":
                continue
            elif s[i] == " ":
                break
            else:
                reach_word = True
                ret += 1
        return ret


solution = Solution().lengthOfLastWord
solution("Hello World")
solution("   fly me   to   the moon  ")
solution("  ")
solution("s")
