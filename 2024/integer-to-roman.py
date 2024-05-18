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
        ch_map = {
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
        i = 0
        ret = ""
        while num > 0:
            ret = "".join(keys[x + i] for x in ch_map[num % 10]) + ret
            num //= 10
            i += 2
        return ret


solution = Solution().intToRoman
# solution(num=3749)
solution(num=58)
solution(num=1994)
