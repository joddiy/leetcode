from tools import *
import pprint


class Solution(object):
    @print_
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        step = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]
        m, n = len(matrix), len(matrix[0])
        cnt = m * n
        cur_step = 0
        ret = []
        i, j = 0, 0
        while cnt > 0:
            if i < 0 or j < 0 or i == m or j == n or matrix[i][j] is None:
                i = i - step[cur_step][0]
                j = j - step[cur_step][1]
                cur_step = (cur_step + 1) % 4
            # output
            else:
                ret.append(matrix[i][j])
                matrix[i][j] = None
                cnt -= 1
            i = i + step[cur_step][0]
            j = j + step[cur_step][1]
        return ret


solution = Solution().spiralOrder
solution(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
solution(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
