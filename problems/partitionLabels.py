from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        indexes = defaultdict(lambda: [n - 1, 0])
        for i, c in enumerate(S):
            indexes[c][0] = min(indexes[c][0], i)
            indexes[c][1] = max(indexes[c][1], i)
        intervals = list(indexes.values())
        intervals = sorted(intervals, key=lambda x: x[0])
        ret = [intervals.pop(0)]
        for tmp in intervals:
            if tmp[0] <= ret[-1][1]:
                if tmp[1] <= ret[-1][1]:
                    continue
                else:
                    ret[-1][1] = tmp[1]
            else:
                ret.append(tmp)
        return [x[1] - x[0] + 1 for x in ret]


solution = Solution().partitionLabels

solution("ababcbacadefegdehijhklij")
solution("a")