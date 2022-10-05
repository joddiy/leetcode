from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hashMap = defaultdict(int)
        result = 0
        for a in A:
            for b in B:
                hashMap[a+b] += 1
                
        for c in C:
            for d in D:
                complement = -(c+d)
                if complement in hashMap:
                    result += hashMap[complement]
        
        return result