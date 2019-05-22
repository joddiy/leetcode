class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ['[', '{', '(']:
                stack.append(c)
            else:
                if not stack:
                    return False
                n = stack.pop()
                if c == ']' and n != '[':
                    return False
                elif c == '}' and n != '{':
                    return False
                elif c == ')' and n != '(':
                    return False
        return not stack

Solution().isValid("[")
