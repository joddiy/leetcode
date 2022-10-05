from tools import *


class Solution(object):
    @print_
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []

        def recursive(l, r, prefix):
            if l == 0 and r == 0:
                ret.append(prefix)
            if l > 0:
                recursive(l - 1, r + 1, prefix + "(")
            if r > 0:
                recursive(l, r - 1, prefix + ")")

        recursive(n, 0, "")
        return ret


solution = Solution().generateParenthesis

solution(3)
solution(1)
