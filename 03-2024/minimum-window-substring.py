import math
import pprint
import sys

from tools import *
from collections import *

import heapq


class Solution(object):
    @print_
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(s)
        count = len(t)
        count_w = Counter(t)
        b, l = 0, sys.maxsize
        i, j = 0, 0
        while j < n:
            if count_w[s[j]] > 0:
                count -= 1
            count_w[s[j]] -= 1

            while count == 0:
                if j - i + 1 < l:
                    l = j - i + 1
                    b = i
                count_w[s[i]] += 1
                if count_w[s[i]] > 0:
                    count += 1
                i += 1
            j += 1
        if l != sys.maxsize:
            return s[b:b + l]
        else:
            return ""


solution = Solution().minWindow
solution(s="ADOBECODEBANC", t="ABC")
# solution(s="a", t="a")
# solution(s="a", t="aa")
