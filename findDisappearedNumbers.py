class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            # index = abs(nums[i]) - 1
            # nums[index] = - abs(nums[index])
            nums[abs(nums[i]) - 1] = - abs(nums[abs(nums[i]) - 1])

        j = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                nums[j] = i + 1
                j += 1
        return nums[:j]


print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
