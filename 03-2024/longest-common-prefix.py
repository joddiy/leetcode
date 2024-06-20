import sys

from tools import *
import pprint


class Solution(object):
    @print_
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n == 1:
            return strs[0]
        min_len = min(len(x) for x in strs)
        ret = ""
        for i in range(min_len):
            cur_c = None
            for j in range(n):
                if cur_c is None:
                    cur_c = strs[j][i]
                elif cur_c != strs[j][i]:
                    return ret
            ret = ret + cur_c
        return ret


solution = Solution().longestCommonPrefix
solution(strs=["flower", "flow", "flight"])
solution(strs=["dog", "racecar", "car"])
solution(strs=["cir", "car"])
