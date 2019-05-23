class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1

        def recursion(s, e):
            if e < s:
                return -1
            m = (s+e)//2
            if nums[m] == target:
                return m
            if nums[s] <= target < nums[m]:
                return recursion(s, m-1)
            elif nums[m] < target <= nums[e]:
                return recursion(m+1, e)
            elif nums[m] > nums[e]:
                return recursion(m+1, e)
            else:
                return recursion(s, m-1)

        return recursion(start, end)


Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
