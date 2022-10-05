from tools import *


class Solution(object):
    @print_
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [""]
        num = ""
        for c in s:
            if c.isdigit():
                num += c
            elif c == "[":
                stack.extend([num, ""])
                num = ""
            elif c == "]":
                chars = stack.pop()
                n_chars = stack.pop()
                stack[-1] += chars * int(n_chars)
            else:
                stack[-1] += c
        return stack.pop()


solution = Solution().decodeString

solution("3[a]2[bc]")
solution("3[a2[c]]")