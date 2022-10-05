from collections import defaultdict, Counter
import heapq
from tools import *


class Solution(object):
    @print_
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        heap_ = []
        i = 0
        for key, val in count.items():
            if i < k:
                heapq.heappush(heap_, (val, key))
            else:
                heapq.heappushpop(heap_, (val, key))
            i += 1
        return [v for k, v in heap_]


solution = Solution().topKFrequent

solution([1, 1, 1, 2, 2, 3], 2)
# solution([1], 1)
