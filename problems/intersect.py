from tools import *
from collections import Counter


class Solution(object):
    @print_
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        count = Counter(nums1)
        ret = []
        for num in nums2:
            if count[num] > 0:
                ret.append(num)
                count[num] -= 1
        return ret


solution = Solution().intersect

solution([1, 2, 2, 1], [2, 2])
