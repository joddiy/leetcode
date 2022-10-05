from tools import *


class Solution(object):
    @print_
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        n = len(T)
        ret = [0] * n
        stack = [(T[-1], n - 1)]
        for i in range(n - 2, -1, -1):
            if T[i] >= stack[-1][0]:
                while stack and T[i] >= stack[-1][0]:
                    stack.pop()
            if stack:
                ret[i] = stack[-1][1] - i

            stack.append((T[i], i))
        return ret


solution = Solution().dailyTemperatures
# solution([73, 74, 75, 71, 69, 72, 76, 73])
# solution([73])
solution([89, 62, 70, 58, 47, 47, 46, 76, 100, 70])
