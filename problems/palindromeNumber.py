from tools import *


class Solution(object):
    @print_
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True

        y = x
        res = []
        while y > 0:
            res.append(y % 10)
            y = y // 10

        return res == res[::-1]


solution = Solution().isPalindrome

solution(121)
solution(1221)
solution(123421)
