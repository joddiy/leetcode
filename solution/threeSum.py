class Solution(object):

    # O(n^2)
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
            if i > 0 and nums[i] == nums[i-1]:  # avoid repeat
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

     # same idea, O(n^2)
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: # avoid repeat
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]: # avoid repeat
                        l += 1
                    while l < r and nums[r] == nums[r-1]: # avoid repeat
                        r -= 1
                    l += 1
                    r -= 1
        return res


Solution().threeSum([-2, 0, 0, 2, 2])
