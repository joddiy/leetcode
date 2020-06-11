from utils.tools import *


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        left, right, height = [0]*n, [n]*n, [0]*n
        maxA = 0
        for i in range(0, m):
            cur_left, cur_right = 0, n
            for j in range(0, n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            for j in range(0, n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j+1
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            for j in range(0, n):
                maxA = max(maxA, (right[j]-left[j])*height[j])
        return maxA

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix or not matrix[0]:
            return 0

        n = len(matrix[0])

        areas = [0] * (n+1)
        area = 0

        for row in matrix:
            areas = [areas[i] + 1 if row[i] ==
                     '1' else 0 for i in range(n)] + [0]
            ps = [-1]
            for p in range(n+1):
                while areas[p] < areas[ps[-1]]:
                    pp = ps.pop()
                    area_pp = (p - ps[-1] - 1) * areas[pp]
                    if area_pp > area:
                        area = area_pp
                ps.append(p)

        return area


Solution().maximalRectangle([
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
])
