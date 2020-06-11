class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = 0
        max_ending_here = 0
        for i in range(len(nums)):
            max_ending_here += nums[i]
            if max_ending_here < 0:
                max_ending_here = 0
            elif max_so_far < max_ending_here:
                max_so_far = max_ending_here
        if max_so_far == 0:
            return max(nums)
        return max_so_far

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(0, nums[i-1]) + nums[i]
            ret = max(ret, nums[i])
        return ret


print(Solution().maxSubArray([-1, 1]))
