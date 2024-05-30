import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        number_map = {
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        ret = []

        def recursive(i, prefix):
            if i == len(digits):
                ret.append(prefix)
            else:
                n = digits[i]
                for c in number_map[n]:
                    recursive(i + 1, prefix + c)

        recursive(0, "")
        return ret


solution = Solution().letterCombinations
solution(digits="23")
solution(digits="")
solution(digits="2")
