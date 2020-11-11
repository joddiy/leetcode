from tools import *


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution(object):
    @print_
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


solution = Solution().largestNumber

solution([10, 2])
solution([3, 30, 34, 5, 9])
