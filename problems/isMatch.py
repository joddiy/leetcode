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

        def match(i, j):
            if j == m:
                return i == n
            elif (i, j) not in memo:
                first_match = i < n and p[j] in (s[i], '.')
                # with '*'
                if j + 1 < m and p[j + 1] == '*':
                    if first_match:
                        res = match(i, j + 2) or match(i + 1, j)
                    else:
                        res = match(i, j + 2)
                else:  # without '*'
                    if first_match:
                        res = match(i + 1, j + 1)
                    else:
                        res = False
                memo[i, j] = res
            return memo[i, j]

        return match(0, 0)


solution = Solution().isMatch

# solution("aa", "a")
solution("aa", "a*")
# solution("ab", ".*")
# solution("aab", "c*a*b")
# solution("mississippi", "mis*is*p*.")
