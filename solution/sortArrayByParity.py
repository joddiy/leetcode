# -*- coding: utf-8 -*-
# file: sortArrayByParity.py
# author: joddiyzhang@gmail.com
# time: 2018/11/20 5:28 PM
# ------------------------------------------------------------------------

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 == 0:
                i += 1
                continue
            if A[j] % 2 == 1:
                j -= 1
                continue
            A[i], A[i] = A[i], A[j]
            i += 1
            j -= 1
        return A


print(Solution().sortArrayByParity([3, 1, 2, 4]))
