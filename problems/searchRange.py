from tools import *


class Solution(object):
    @print_
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return (-1, -1)

        n = len(nums)

        def find_left(i, j):
            if i > j:
                return i
            else:
                m = (i + j) // 2
                if nums[m] >= target:
                    return find_left(i, m - 1)
                else:
                    return find_left(m + 1, j)

        def find_right(i, j):
            if i > j:
                return j
            else:
                m = (i + j) // 2
                if nums[m] <= target:
                    return find_right(m + 1, j)
                else:
                    return find_right(i, m - 1)

        l, r = find_left(0, n - 1), find_right(0, n - 1)
        return (l, r) if l <= r else (-1, -1)


solution = Solution().searchRange

solution([5, 7, 7, 8, 8, 10], 8)
solution([5, 7, 7, 8, 8, 10], 6)
solution([], 0)
