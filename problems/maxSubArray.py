from tools import *
import sys


class Solution(object):
    # O(n)
    @print_
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = 0
        least_sum = 0
        ret = -sys.maxsize
        for i in range(len(nums)):
            cur_sum += nums[i]
            ret = max(ret, cur_sum - least_sum)
            # update least_sum after the ret
            # because we don't want cur_sum - cur_sum
            least_sum = min(least_sum, cur_sum)
        return ret

    # divide and conquer
    # nlog(n)
    @print_
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        def recursive(i, j):
            if j <= i:
                return nums[i]

            m = (i + j) // 2
            lmax = recursive(i, m - 1)
            rmax = recursive(m + 1, j)

            lsum = 0
            sum_ = 0
            for i in range(m - 1, -1, -1):
                sum_ += nums[i]
                lsum = max(lsum, sum_)

            rsum = 0
            sum_ = 0
            for i in range(m + 1, n):
                sum_ += nums[i]
                rsum = max(rsum, sum_)

            return max(lmax, rmax, lsum + rsum + nums[m])

        return recursive(0, n - 1)


solution = Solution().maxSubArray

solution([-2, 1, -3, 4, -1, 2, 1, -5, 4])
solution([1])
solution([-1])
solution([-2, -1])
solution([1, 2])
solution([1, -2])
solution([-1, 2])