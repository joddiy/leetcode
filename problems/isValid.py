from tools import *


class Solution(object):
    @print_
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if not stack:
                    return False
                cc = stack.pop(-1)
                if cc == "(" and c != ")":
                    return False
                elif cc == "[" and c != "]":
                    return False
                elif cc == "{" and c != "}":
                    return False
        return not stack

solution = Solution().isValid

solution(r"()[]{}")