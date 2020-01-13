class Solution(object):
    # O(nlogn)
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        j = 1
        for i in nums:
            if i < j:
                continue
            elif i == j:
                j += 1
            else:
                return j
        return j

    # O(n)
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):  # delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        # use the index as the hash to record the frequency of each number
        for i in range(len(nums)):
            nums[nums[i] % n] += n # +n and %n to make the original value do not be overlaped
        for i in range(1, len(nums)):
            if nums[i] < n:
                return i
        return n


print(Solution().firstMissingPositive([1,2,0]))
