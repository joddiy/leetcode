from tools import *


class Solution(object):
    @print_
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        ret = []
        for p in people:
            ret.insert(p[1], p)
        return ret

solution = Solution().reconstructQueue

solution([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
