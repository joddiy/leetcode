from tools import *


class Solution(object):
    @print_
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip('0')
        if not s:
            return 0
        ret = 1
        for i in range(len(s)):
            if s[i] == '0' or (i >= 1 and s[i - 1] == '0'):
                continue
            if i >= 1 and int(s[i - 1:i + 1]) <= 26:
                ret += 1
        return ret


solution = Solution().numDecodings

# solution("12")
# solution("226")
# solution("326")
# solution("1")

# solution("206")
# solution("20")
# solution("0")
# solution("00")
# solution("002")
solution("2101")