from tools import *


class Solution(object):
    @print_
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums = sorted(nums)
        ret = []
        for i in range(n - 2):
            # skip the repeat num
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ < 0:
                    j += 1
                elif sum_ > 0:
                    k -= 1
                else:
                    ret.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return ret


solution = Solution().threeSum

solution([-1, 0, 1, 2, -1, -4])
solution([1, 2, -2, -1])
solution([-1, 0, 1, 0])
