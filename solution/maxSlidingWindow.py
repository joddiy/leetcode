class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_v = []
        if not nums:
            return max_v
        for i in range(0, len(nums)-k+1):
            max_v.append(max(nums[i:i+k]))
        return max_v

    #
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return nums

        result = [max(nums[:k])]

        for i in range(len(nums)-k):
            if nums[i+k] > result[-1]:
                result.append(nums[i+k])
                i += 1
            elif nums[i] < result[-1]:
                result.append(result[-1])
                i += 1
            else:
                i += 1
                result.append(max(nums[i:i+k]))

        return result


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
