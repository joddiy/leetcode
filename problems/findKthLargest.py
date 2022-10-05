from tools import *
import heapq


class Solution(object):
    # O(nlogk)
    @print_
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap_ = nums[:k]
        heapq.heapify(heap_)
        for i in range(k, len(nums)):
            heapq.heappushpop(heap_, nums[i])
        return heapq.heappop(heap_)

    # O(2n)
    @print_
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def select(nums, k):
            m = nums.pop(len(nums) // 2)
            larger = [n for n in nums if n > m]
            ll = len(larger)
            if k <= ll:
                return select(larger, k)
            elif k == ll + 1:
                return m
            else:
                less = [n for n in nums if n <= m]
                return select(less, k - ll - 1)

        return select(nums, k)


solution = Solution().findKthLargest
solution([3, 2, 1, 5, 6, 4], 2)
solution([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
