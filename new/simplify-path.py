import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for p in path.split("/"):
            if not p or p == '.':
                continue
            elif p == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)

        return "/" + "/".join(stack)


solution = Solution().simplifyPath
solution(path="/home/")
solution(path="/../")
solution("/home//foo/")
