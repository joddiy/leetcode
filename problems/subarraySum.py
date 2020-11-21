from tools import *


class Solution(object):
    # O(n^2)
    @print_
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cache = {0: 1}
        cur_sum = 0
        ret = 0
        for n in nums:
            cur_sum += n
            ret += cache.get(cur_sum - k, 0)
            cache[cur_sum] = cache.get(cur_sum, 0) + 1
        return ret

    # O(n)
    @print_
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cache = {0: 1}
        cur_sum = 0
        ret = 0
        for n in nums:
            cur_sum += n
            ret += cache.get(cur_sum - k, 0)
            cache[cur_sum] = cache.get(cur_sum, 0) + 1
        return ret


solution = Solution().subarraySum

solution([1, 1, 1], 2)
solution([1], 1)