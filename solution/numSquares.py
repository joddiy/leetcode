import math
import sys


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        nums = [i*i for i in range(1, int(math.ceil(math.sqrt(n)))+1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            least_num = sys.maxsize
            for j in range(len(nums)):
                if i - nums[j] < 0:
                    break
                least_num = min(least_num, dp[i - nums[j]])
            dp[i] = least_num + 1
        return dp[-1]


print(Solution().numSquares(12))
