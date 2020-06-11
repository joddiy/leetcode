class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, k, j = 0, 0, len(nums)-1
        while k <= j:
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k += 1
            elif nums[k] == 1:
                k += 1
            elif nums[k] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1
        return nums


print(Solution().sortColors([1, 0, 2]))
