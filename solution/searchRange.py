class Solution(object):
    # case 1, iteration
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x > A[mid]:
                    left = mid + 1
                else:  # if we found the value, we still check its left part to find the first one
                    right = mid - 1
            return left

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x >= A[mid]:  # if we found the value, we still check its right part to find the last one
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left, right = binarySearchLeft(
            nums, target), binarySearchRight(nums, target)
        # once we cannot found the value, the left will right-1
        return [left, right] if left <= right else [-1, -1]

    # case 2, recursion
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def recursiveLeft(s, e):
            if e < s:
                return s
            m = (s+e)//2
            if nums[m] < target:
                return recursiveLeft(m+1, e)
            else:
                return recursiveLeft(s, m-1)

        def recursiveRight(s, e):
            if e < s:
                return e
            m = (s+e)//2
            if nums[m] <= target:
                return recursiveRight(m+1, e)
            else:
                return recursiveRight(s, m-1)

        left, right = recursiveLeft(0, len(nums)-1), recursiveRight(0, len(nums)-1)
        # once we cannot found the value, the left will right-1
        return [left, right] if left <= right else [-1, -1]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], -1))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 7.5))
