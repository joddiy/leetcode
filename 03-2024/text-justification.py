import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result, cur, cnt = [], [], 0
        for word in words:
            if cnt + len(cur) + len(word) > maxWidth:
                for i in range(maxWidth - cnt):
                    if len(cur) == 1:
                        cur[0] += ' '
                    else:
                        cur[i % (len(cur) - 1)] += ' '
                result.append(''.join(cur))
                cur, cnt = [], 0
            cur.append(word)
            cnt += len(word)

        return result + [' '.join(cur).ljust(maxWidth)]


solution = Solution().fullJustify
solution(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16)
solution(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16)
