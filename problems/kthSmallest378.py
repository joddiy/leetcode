from tools import *


class Solution(object):
    @print_
    def kthSmatrixllest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)

        def check(mid):
            r, c = n - 1, 0
            nums = 0
            while r >= 0 and c < n:
                if matrix[r][c] <= mid:
                    nums += r + 1
                    c += 1
                else:
                    r -= 1
            return nums >= k

        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


solution = Solution().kthSmatrixllest

# solution([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)
solution([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 3)
