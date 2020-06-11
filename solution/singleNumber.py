# -*- coding: utf-8 -*-
# file: singleNumber.py
# author: joddiyzhang@gmail.com
# time: 2018/11/20 6:13 PM
# ------------------------------------------------------------------------

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i in nums:
            ret ^= i
        return ret


print(Solution().singleNumber([2, 2, 1]))
