# -*- coding: utf-8 -*-
# file: judgeCircle.py
# author: joddiyzhang@gmail.com
# time: 2018/11/20 5:39 PM
# ------------------------------------------------------------------------

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
