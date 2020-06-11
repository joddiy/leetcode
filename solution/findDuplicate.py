class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set()
        for i in nums:
            if i not in numSet:
                numSet.add(i)
            else:
                return i

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype:
        """
        slow = nums[0]  # 1 step from start point
        fast = nums[nums[0]]  # 2 steps from start point
        while slow != fast:
            slow = nums[slow]  # 1 step
            fast = nums[nums[fast]]  # 2 steps
        slow = 0
        while slow != fast:
            slow = nums[slow]  # 1 step
            fast = nums[fast]  # 1 step
        return slow

    # def findDuplicate(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype:
    #     """
    #     while nums[nums[0]] != nums[0]:
    #         nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
    #     return nums[0]


print(Solution().findDuplicate([3, 1, 3, 4, 2]))
