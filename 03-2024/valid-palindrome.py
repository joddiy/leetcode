from tools import *


class Solution(object):
    @print_
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = "".join(x for x in s if ('a' <= x <= 'z') or ('0' <= x <= '9'))
        i = 0
        while i < len(s) // 2:
            if s[i] == s[-i - 1]:
                i += 1
            else:
                return False
        return True


solution = Solution().isPalindrome
# solution(s="A man, a plan, a canal: Panama")
# solution(s="race a car")
# solution(s = " ")

# solution(s="abba")
solution(s="0p")
# solution(s="aba")
