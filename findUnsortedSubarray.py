class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        l, r = 0, len(nums) - 1
        while l < len(nums) - 1 and nums[l] <= nums[l + 1]:
            l += 1
        while r > 0 and nums[r] >= nums[r - 1]:
            r -= 1
        if l > r:
            return 0
        temp = nums[l:r+1]
        tempMin = min(temp)
        tempMax = max(temp)
        while l > 0 and tempMin < nums[l-1]:
            l -= 1
        while r < len(nums) - 1 and tempMax > nums[r+1]:
            r += 1

        return r - l + 1

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        cur_max = nums[0]
        right = 0
        for i in range(1, len(nums)):
            if nums[i] < cur_max:
                right = i
            cur_max = max(cur_max, nums[i])

        cur_min = nums[-1]
        left = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > cur_min:
                left = i
            cur_min = min(cur_min, nums[i])
        return max(right-left+1, 0)


print(Solution().findUnsortedSubarray(
    [2, 6, 4, 8, 10, 9, 15]))
