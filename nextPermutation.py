class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[:i:-1]
        print(nums)

    class Solution(object):
        def nextPermutation(self, num):
            k, l = -1, 0
            for i in range(len(num) - 1):
                if num[i] < num[i + 1]:
                    k = i

            if k == -1:
                num.reverse()
                return

            for i in range(k + 1, len(num)):
                if num[i] > num[k]:
                    l = i

            num[k], num[l] = num[l], num[k]
            num[k + 1:] = num[:k:-1]


Solution().nextPermutation([1, 3, 2])
