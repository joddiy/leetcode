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
        if not strs:
            return ""
        nstr = len(strs)
        ret = ""
        s_len = min(len(str) for str in strs)
        for i in range(s_len):
            cur_c = strs[0][i]
            for j in range(1, nstr):
                if cur_c != strs[j][i]:
                    cur_c = ""
                    break
            if cur_c != "":
                ret = ret + cur_c
            else:
                break
        return ret


solution = Solution().longestCommonPrefix
# solution(strs=["flower", "flow", "flight"])
# solution(strs=["dog", "racecar", "car"])
solution(strs=["cir", "car"])
