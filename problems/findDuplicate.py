class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        ret = 0
        while slow != ret:
            slow = nums[slow]
            ret = nums[ret]
        return ret


solution = Solution().findDuplicate

solution([1, 3, 4, 2, 2])