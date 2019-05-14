

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        k_heap = nums[0:k]
        heapq.heapify(k_heap)
        for i in range(k, len(nums)):
            heapq.heappush(k_heap, nums[i])
            heapq.heappop(k_heap)
        return heapq.heappop(k_heap)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quickselect(nums, k):
            pivot = nums.pop(len(nums) // 2)
            left = [n for n in nums if n > pivot]
            ll = len(left)
            if ll == k-1:
                return pivot

            elif ll > k - 1:
                return quickselect(left, k)
            else:
                return quickselect([n for n in nums if n <= pivot], k - ll - 1)
        return quickselect(nums, k)


Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
