class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                pop_stack = []
                n_n = 0
                while True:
                    n_c = stack.pop()
                    if n_c != '[':
                        pop_stack.append(n_c)
                    else:
                        base = 1
                        while True:
                            if stack and stack[-1].isdigit():
                                n_n += base * int(stack.pop())
                                base *= 10
                            else:
                                break
                        pop_stack = pop_stack*n_n
                        break
                stack.extend(pop_stack[::-1])
        return ''.join(stack)


Solution().decodeString('100[leetcode]')
