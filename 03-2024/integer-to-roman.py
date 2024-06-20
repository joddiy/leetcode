import sys

from tools import *
import pprint


class Solution(object):
    @print_
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        keys = ["I", "V", "X", "L", "C", "D", "M"]
        # I, II, III, IV, V, VI, VII, VIII, IX
        offset = {
            0: [],
            1: [0],
            2: [0, 0],
            3: [0, 0, 0],
            4: [0, 1],
            5: [1],
            6: [1, 0],
            7: [1, 0, 0],
            8: [1, 0, 0, 0],
            9: [0, 2],
        }
        ret = []
        i = 0
        while num:
            cur = num % 10
            cur_sign = "".join(keys[i + x] for x in offset[cur])
            ret.insert(0, cur_sign)
            num //= 10
            i += 2
        return "".join(ret)


solution = Solution().intToRoman
solution(num=3749)
# solution(num=58)
# solution(num=1994)
