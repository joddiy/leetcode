from tools import *


class Solution(object):
    @print_
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        while tokens:
            c = tokens.pop(0)
            if c not in "+-*/":
                stack.append(int(c))
            else:
                p2 = stack.pop(-1)
                p1 = stack.pop(-1)
                if c == '+':
                    ret = p1 + p2
                elif c == '-':
                    ret = p1 - p2
                elif c == '*':
                    ret = p1 * p2
                else:
                    ret = int(float(p1) / p2)
                stack.append(ret)
        return stack[-1]


solution = Solution().evalRPN

# solution(["2", "1", "+", "3", "*"])
# solution(["4", "13", "5", "/", "+"])
solution(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
