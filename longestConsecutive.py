class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lgs = 0
        for num in nums:
            current_num = num
            current_count = 1
            while current_num + 1 in nums:
                current_num += 1
                current_count += 1
            lgs = max(lgs, current_count)

        return lgs

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        lgs = 1
        current_count = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_count += 1
                else:
                    lgs = max(lgs, current_count)
                    current_count = 1

        return max(lgs, current_count)

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lgs = 0
        num_set = set(nums)
        for num in num_set:
            if num -1 not in num_set:
                current_num = num
                current_count = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_count += 1
                lgs = max(lgs, current_count)

        return lgs



Solution().longestConsecutive([100,4,200,1,3,2])
