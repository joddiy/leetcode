from tools import *


class Solution(object):
    @print_
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        ret = []
        c1, r1, c2, r2 = 0, 0, len(matrix[0]) - 1, len(matrix) - 1
        while c1 <= c2 and r1 <= r2:
            for c in range(c1, c2 + 1):
                ret.append(matrix[r1][c])
            for r in range(r1 + 1, r2 + 1):
                ret.append(matrix[r][c2])
            # once c1 == c2 or r1 == r2
            # there will be at same column or
            # same row with the above two iteration
            if c1 < c2 and r1 < r2:
                for c in range(c2 - 1, c1 - 1, -1):
                    ret.append(matrix[r2][c])
                for r in range(r2 - 1, r1, -1):
                    ret.append(matrix[r][c1])
            c1 += 1
            c2 -= 1
            r1 += 1
            r2 -= 1
        return ret


solution = Solution().spiralOrder

solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

solution([[]])

solution([[1]])

solution([[1, 2, 3]])

solution([[1, 2, 3], [4, 5, 6]])

solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
