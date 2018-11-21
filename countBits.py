# -*- coding: utf-8 -*-
# file: countBits.py
# author: joddiyzhang@gmail.com
# time: 2018/11/21 1:09 PM
# ------------------------------------------------------------------------

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        f = [0]
        for i in range(1, num):
            f.append(f[i // 2] + i % 2)
        return f


print(Solution().countBits(5))
