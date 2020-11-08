from tools import *


class Solution(object):
    @print_
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def recursive(i):
            if i == 1:
                return "1"
            tmp = recursive(i - 1) + "#"
            ret = ""
            count = 1
            current_c = tmp[0]
            for i in range(1, len(tmp)):
                c = tmp[i]
                if c != current_c:
                    ret += str(count) + current_c
                    current_c = c
                    count = 1
                else:
                    count += 1
            return ret

        return recursive(n)


solution = Solution().countAndSay

solution(1)
solution(2)
solution(3)
solution(4)