from tools import *


class Solution(object):
    @print_
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n, m = len(s), len(p)
        memo = {}

        def recusive(i, j):
            if i == n and j == m:
                return True
            elif i != n and j == m:
                return False
            elif (i, j) not in memo:
                first_match = i < n and p[j] in (".", s[i])
                # with '*'
                if j + 1 < m and p[j + 1] == '*':
                    if first_match:
                        res = recusive(i, j + 2) or recusive(i + 1, j)
                    else:
                        res = recusive(i, j + 2)
                # without '*'
                else:
                    if first_match:
                        res = recusive(i + 1, j + 1)
                    else:
                        res = False
                memo[i, j] = res
            return memo[i, j]

        return recusive(0, 0)


solution = Solution().isMatch

# solution("aa", "a")
solution("aa", "a*")
# solution("ab", ".*")
# solution("aab", "c*a*b")
# solution("mississippi", "mis*is*p*.")
