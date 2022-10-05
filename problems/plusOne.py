from tools import *


class Solution(object):
    @print_
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            sum_ = digits[i] + carry
            digits[i] = sum_ % 10
            carry = sum_ // 10
        if carry:
            digits.insert(0, carry)

        return digits


solution = Solution().plusOne

solution([1, 2, 3])
solution([4, 3, 2, 1])
solution([1, 2, 9])
solution([0])
solution([9])