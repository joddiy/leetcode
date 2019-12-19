class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        bucket_key = None
        bucket_cnt = 0
        for i in range(len(nums)):
            if bucket_cnt == 0:
                bucket_key = nums[i]
                bucket_cnt = 1
            elif nums[i] == bucket_key:
                bucket_cnt += 1
            else:
                bucket_cnt -= 1
        return bucket_key


print(Solution().majorityElement([6, 5, 5]))
