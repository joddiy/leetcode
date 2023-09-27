import pprint

from tools import *


class Solution(object):
    @print_
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        keys = ["I", "V", "X", "L", "C", "D", "M"]
        quick_map = {
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
        offset = 0
        ret = ""
        while num > 0:
            left = num % 10
            ret = "".join(keys[offset + i] for i in quick_map[left]) + ret
            num = num // 10
            offset += 2
        return ret


solution = Solution().intToRoman
# solution(1)
# solution(3)
# solution(10)
# solution(58)
solution(100)
# solution(1994)
# solution(3999)
