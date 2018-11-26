# -*- coding: utf-8 -*-
# file: permute.py
# author: joddiyzhang@gmail.com
# time: 2018/11/26 10:45 AM
# ------------------------------------------------------------------------

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
