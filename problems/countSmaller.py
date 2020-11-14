from tools import *


class Solution(object):
    # O(n^2)
    @print_
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ret = []
        for i in range(n):
            sum_ = 0
            for j in range(i, n):
                if nums[j] < nums[i]:
                    sum_ += 1
            ret.append(sum_)
        return ret

    # O(n^logn) stable sort(merge sort)
    @print_
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

    # O(n^logn) stable sort(merge sort)
    @print_
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = []
        n = len(nums)
        output = [0] * n
        for i in range(n - 1, -1, -1):
            output[i] = bisect.bisect_left(temp, nums[i])
            temp[output[i]:output[i]] = [nums[i]]
        return output


solution = Solution().countSmaller

solution([5, 2, 6, 1])
