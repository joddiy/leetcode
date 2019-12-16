# -*- coding: utf-8 -*-
# file: subsets.py
# author: joddiyzhang@gmail.com
# time: 2018/11/26 11:02 AM
# ------------------------------------------------------------------------


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def recursive(nums, index, path, res):
            res.append(path)
            for i in range(index, len(nums)):
                recursive(nums, i + 1, path + [nums[i]], res)

        res = []
        recursive(sorted(nums), 0, [], res)
        return res


print(Solution().subsets([1, 2, 3]))
