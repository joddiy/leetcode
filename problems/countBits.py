from tools import *


class Solution(object):
    @print_
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i // 2] + i % 2
        return dp

solution = Solution().countBits

solution(2)
solution(5)
