# -*- coding: utf-8 -*-
# file: generateParenthesis.py
# author: joddiyzhang@gmail.com
# time: 2018/11/26 11:19 AM
# ------------------------------------------------------------------------

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def recursive(n, stack, path, res):
            if stack == 0 and n == 0:
                res.append(path)
                return
            if stack != 0 and n == 0:
                recursive(n, stack - 1, path + ")", res)
            elif stack == 0 and n > 0:
                recursive(n - 1, stack + 1, path + "(", res)
            else:
                recursive(n - 1, stack + 1, path + "(", res)
                recursive(n, stack - 1, path + ")", res)

        res = []
        recursive(n, 0, "", res)
        return res
