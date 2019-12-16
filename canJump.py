class Solution(object):
    # O(n)
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = 0
        for i in range(0, len(nums)):
            if i > m:
                return False
            m = max(m, i+nums[i])
        return True


print(Solution().canJump([1, 2]))
