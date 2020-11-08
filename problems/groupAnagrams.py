from tools import *

class Solution(object):
    @print_
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = {}
        for s in strs:
            tmp = tuple(sorted(s))
            if tmp not in ret:
                ret[tmp] = []
            ret[tmp].append(s)
        return list(ret.values())


groupAnagrams = Solution().groupAnagrams

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
groupAnagrams(["cab", "pug", "pei", "nay", "ron", "rae", "ems", "ida", "mes"])