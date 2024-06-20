import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ("(", "{", "["):
                stack.append(c)
            else:
                if not stack:
                    return False
                c_ = stack.pop(-1)
                if (c_ == "(" and c != ")") or (c_ == "[" and c != "]") or (c_ == "{" and c != "}"):
                    return False
        return len(stack) == 0


solution = Solution().isValid
solution(s="()")
solution(s="()[]{}")
solution(s="(]")
