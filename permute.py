class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recursive(nums, path, res):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                recursive(nums[:i] + nums[i + 1:], path + [nums[i]], res)

        res = []
        recursive(nums, [], res)
        return res


print(Solution().permute([1, 2, 3, 4, 5]))
