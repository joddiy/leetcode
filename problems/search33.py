from tools import *


class Solution(object):
    @print_
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        def find(i, j):
            if i > j:
                return -1
            else:
                m = (i + j) // 2
                m_v = nums[m]
                if m_v == target:
                    return m
                # target at left, and pivot at right
                elif nums[i] <= target < m_v:
                    return find(i, m - 1)
                # target at right, and pivot at left
                elif m_v < target <= nums[j]:
                    return find(m + 1, j)
                # target at left, and pivot at left
                elif m_v <= nums[j]:
                    return find(i, m - 1)
                # target at right, and pivot at right
                elif nums[i] <= m_v:
                    return find(m + 1, j)

        return find(0, n - 1)


solution = Solution().search

solution([4, 5, 6, 7, 0, 1, 2], 0)
solution([6, 7, 0, 1, 2, 4, 5], 0)
solution([5, 6, 7, 0, 1, 2, 4], 0)
solution([4, 5, 6, 7, 0, 1, 2], 3)
solution([1], 0)
solution([5, 1, 3], 3)