from utils.tools import *


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        for i in range(0, n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                if sum == k:
                    count += 1
        return count

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash_map = {0: 1}
        curr_sum = 0
        ret = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            offset = curr_sum - k
            if offset in hash_map:
                ret += hash_map[offset]
            if curr_sum in hash_map:
                hash_map[curr_sum] += 1
            else:
                hash_map[curr_sum] = 1
        return ret


Solution().subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7)
