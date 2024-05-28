import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map_ = defaultdict(list)
        for s in strs:
            map_["".join(sorted(s))].append(s)
        return list(map_.values())


solution = Solution().groupAnagrams
solution(strs=["eat", "tea", "tan", "ate", "nat", "bat"])
solution(strs=[""])
solution(strs=["a"])
