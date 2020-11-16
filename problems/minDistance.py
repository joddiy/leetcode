from tools import *


class Solution(object):
    @print_
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if m > n:
            m, n, word1, word2 = n, m, word2, word1
        memo = {}

        def recusive(i, j):
            if i == m and j == n:
                return 0
            elif i == m:
                return n - j
            elif j == n:
                return m - i
            elif (i, j) not in memo:
                if word1[i] == word2[j]:
                    res = recusive(i + 1, j + 1)
                else:
                    res = min(
                        recusive(i, j + 1),  # insert
                        recusive(i + 1, j + 1),  #replace
                        recusive(i + 1, j)  # delete
                    ) + 1
                memo[i, j] = res
            return memo[i, j]

        return recusive(0, 0)


solution = Solution().minDistance

solution("horse", "ros")