import pprint

from tools import *


class Solution(object):
    @print_
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len = min([len(str_) for str_ in strs])
        ret = ""
        for i in range(min_len):
            cur_c = None
            for j in range(len(strs)):
                if not cur_c:
                    cur_c = strs[j][i]
                elif strs[j][i] != cur_c:
                    return ret
                else:
                    continue
            ret += cur_c
        return ret


solution = Solution().longestCommonPrefix
solution(["flower", "flow", "flight"])
