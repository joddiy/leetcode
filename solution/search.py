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
            # target locates at non-axis side (and is left side)
            if nums[s] <= target < nums[m]:
                return recursion(s, m-1)
            # target locates at non-axis side (and is right side)
            elif nums[m] < target <= nums[e]:
                return recursion(m+1, e)
            # target locates at axis side (and is right side)
            elif nums[m] > nums[e]:
                return recursion(m+1, e)
            else:  # target locates at axis side (and is left side)
                return recursion(s, m-1)

        return recursion(start, end)


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
