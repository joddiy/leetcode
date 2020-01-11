class Solution(object):
    # O(n^2) time limit exceeded
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                if sum == k:
                    count += 1
        return count

    # O(n), any sum of substring can be got by sum[i, j] = sum[0, j] - sum[0, i]
    # so we just calculate sum[0, i] for i in range(n)
    # each time when we have a sum[0, j], we check whether we have a sum[0, i] already to make sum[i, j] == target, 
    # that is sum[0, i] = sum[0, j] - target, we only need a hash table to store all sum[0, i] to find it. 
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


# print(Solution().subarraySum([1, 1, 1], 2))
print(Solution().subarraySum([1, 2, 3], 3))
print(Solution().subarraySum([1], 1))
print(Solution().subarraySum([1], 0))
