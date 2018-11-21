# -*- coding: utf-8 -*-
# file: reverseString.py
# author: joddiyzhang@gmail.com
# time: 2018/11/20 5:11 PM
# ------------------------------------------------------------------------

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        length = len(s)
        for i in range(length // 2):
            tmp = s[length - i - 1]
            s[length - i - 1] = s[i]
            s[i] = tmp
        return "".join(s)

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


print(Solution().reverseString("hello"))
