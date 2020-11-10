from tools import *
import re


class Solution(object):
    @print_
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        s_ = []

        num = ""
        set_ = set("+-*/")
        signed = 1
        for c in s:
            if c == " ":
                continue
            elif c in set_:
                s_.append(signed * float(num))
                if c == "*" or c == "/":
                    s_.append(c)
                num = ""
                signed = -1 if c == '-' else 1
            else:
                num += c
        s_.append(signed * float(num))

        i = 0
        while i < len(s_):
            if s_[i] == '*':
                ret = stack.pop(-1) * s_[i + 1]
                stack.append(int(ret))
                i += 2
            elif s_[i] == '/':
                ret = stack.pop(-1) / s_[i + 1]
                stack.append(int(ret))
                i += 2
            else:
                stack.append(s_[i])
                i += 1

        return int(sum(stack))


solution = Solution().calculate

solution("3+5 / 2 ")
solution("3-2*2")
