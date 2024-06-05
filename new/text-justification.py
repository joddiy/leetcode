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
        result, cur, n_letters = [], [], 0

        for word in words:
            # len(cur) means space between words
            if n_letters + len(words) + len(cur) > maxWidth:
                for i in range(maxWidth - n_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                result.append(''.join(cur))
                cur, n_letters = [], 0

            cur.append(word)
            n_letters += len(word)

        return result


solution = Solution().fullJustify
solution(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16)
solution(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16)
