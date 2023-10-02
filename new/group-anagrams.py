import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ana_map = defaultdict(list)
        for s in strs:
            ana_map["".join(sorted(s))].append(s)

        ret = []
        for v in ana_map.values():
            ret.append(v)

        return ret


solution = Solution().groupAnagrams
solution(["eat", "tea", "tan", "ate", "nat", "bat"])
solution([""])
solution(["a"])
