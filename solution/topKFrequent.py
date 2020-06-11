class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1

        import heapq
        heap = [(-value, key) for key, value in hash_map.items()]
        largest = heapq.nsmallest(k, heap)
        return [key for value, key in largest]


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
