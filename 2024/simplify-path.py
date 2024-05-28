import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        stack = []
        for p in path:
            if p in ('', '.'):
                continue
            if not stack:
                if p != '..':
                    stack.append(p)
            elif p == '..':
                stack.pop(-1)
            else:
                stack.append(p)
        return "/" + "/".join(stack)


solution = Solution().simplifyPath
solution(path="/home/")
solution(path="/home//foo/")
solution(path="/home/user/Documents/../Pictures")
solution(path="/../")
solution(path="/.../a/../b/c/../d/./")
