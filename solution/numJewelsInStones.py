# -*- coding: utf-8 -*-
# file: numJewelsInStones.py
# author: joddiyzhang@gmail.com
# time: 2018/11/20 5:04 PM
# ------------------------------------------------------------------------

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        setJ = set(J)
        return sum(s in setJ for s in S)
