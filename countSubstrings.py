# -*- coding: utf-8 -*-
# file: countSubstrings.py
# author: joddiyzhang@gmail.com
# time: 2018/11/22 9:08 PM
# ------------------------------------------------------------------------

class Solution(object):

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.count = 0

        def extendPalindrome(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                self.count += 1
                left -= 1
                right += 1

        if s is None or len(s) == 0:
            return 0

        for i in range(len(s)):
            extendPalindrome(s, i, i)
            extendPalindrome(s, i, i + 1)

        return self.count


print(Solution().countSubstrings("abc"))
