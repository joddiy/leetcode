import random


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = nums
        self.reset()

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = [i for i in self.original]
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random.shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3])
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_2)