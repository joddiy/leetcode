import math
import pprint
import sys

from tools import *
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

        def recursive(cur_ret, i):
            if i < len(digits):
                for ch in number_map[digits[i]]:
                    recursive(cur_ret + ch, i + 1)
            else:
                ret.append(cur_ret)

        recursive("", 0)
        return ret


solution = Solution().letterCombinations
solution(digits="23")
solution(digits="2")
solution(digits="")
