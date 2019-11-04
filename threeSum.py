class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums = list(nums)
        nums.sort()
        n = len(nums)
        for i in range(n):
            k = n-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if k <= j:
                    break
                t_sum = nums[i] + nums[j]
                while k > 0 and nums[k] > -t_sum:
                    k -= 1
                if k <= j:
                    break
                if nums[k] == -t_sum:
                    ret.append([nums[i], nums[j], -t_sum])
                    while k > 0 and nums[k] == -t_sum:
                        k -= 1
        return ret




Solution().threeSum([-2, 0, 0, 2, 2])

