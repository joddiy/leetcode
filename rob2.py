class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #1: rob, 2: not rob
        n = len(nums)
        if n == 0:
            return 0
        max_rob, max_not_rob = [0]*n, [0]*n
        max_rob[0] = nums[0]
        max_not_rob[0] = 0
        for i in range(1, n):
            max_rob[i] = max_not_rob[i-1] + nums[i]
            max_not_rob[i] = max(max_not_rob[i-1], max_rob[i-1])
        return max(max_not_rob[-1], max_rob[-1])


Solution().rob([2, 7, 9, 3, 1])
