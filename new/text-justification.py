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
        result, cur, num_of_letters = [], [], 0

        for word in words:
            if num_of_letters + len(word) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                result.append(''.join(cur))
                cur, num_of_letters = [], 0

            cur += [word]
            num_of_letters += len(word)

        return result + [' '.join(cur).ljust(maxWidth)]


solution = Solution().fullJustify
solution(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16)
solution(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16)
