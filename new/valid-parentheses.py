import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = {"(", "[", "{"}
        for c in s:
            if c in left:
                stack.append(c)
            elif not stack:
                return False
            else:
                c_ = stack.pop()
                if (c_ == "(" and c == ")") or (c_ == "[" and c == "]") or (c_ == "{" and c == "}"):
                    continue
                else:
                    return False
        if stack:
            return False
        else:
            return True


solution = Solution().isValid
solution(s="()")
solution(s="()[]{}")
solution(s="(]")
solution(s="]")
