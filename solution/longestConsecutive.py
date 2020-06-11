class Solution(object):
    # 40 ms
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lgs = 0
        num_set = set(nums)
        for num in nums:
            if num - 1 not in num_set:
                current_num = num
                current_count = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_count += 1
                lgs = max(lgs, current_count)

        return lgs


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
