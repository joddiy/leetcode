from tools import *
from collections import defaultdict


class Solution(object):
    # O(n^2)
    @print_
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        map_ = defaultdict(list)
        n = len(s)
        # dp[start][length-1] is Palindrome
        dp = [[False] * n for _ in range(n)]

        # length = 1
        for i in range(n):
            dp[i][0] = True
            map_[i].append(1)

        # length = 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][1] = True
                map_[i].append(2)

        # lenght > 2
        for l in range(3, n + 1):
            for i in range(0, n - l + 1):
                if dp[i + 1][l - 3] and s[i] == s[i + l - 1]:
                    dp[i][l - 1] = True
                    map_[i].append(l)

        ret = []

        def find(i, prefix):
            if i >= n:
                ret.append(prefix)
                return
            for l in map_[i]:
                find(i + l, prefix + [s[i:i + l]])

        for l in map_[0]:
            find(l, [s[:l]])

        return ret


solution = Solution().partition

# solution("aab")
solution("aaaa")
