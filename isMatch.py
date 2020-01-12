class Solution(object):

    # cannot handle multi-branch match
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n, m = 0, 0
        while n <= len(s) - 1 and m <= len(p) - 1:
            if p[m] == '.' or p[m] == s[n]:
                n += 1
                if m+1 <= len(p)-1 and p[m+1] == '*':
                    continue
                m += 1
            else:
                if p[m+1] == '*':
                    m += 2
                else:
                    return False
        if n <= len(s) - 1:
            return False
        while m <= len(p) - 1:
            if m+1 <= len(p) - 1 and p[m+1] == '*':
                m += 2
            elif p[m] == '.':
                m += 1
            else:
                return False
        return True

    # still cannot
    def isMatch(self, s, p):
        _p = []
        i = len(p)-1
        while i > -1:
            if p[i] == '*':
                _p.insert(0, p[i-1:i+1])
                i -= 2
            else:
                _p.insert(0, p[i])
                i -= 1

        def recusive(s, p, i, j, memo):
            if i == -1 and j == -1:
                return True
            if j == -1 and i != -1:
                return False
            if i == -1 and j != -1:
                while j > -1 and p[j][-1] == '*':
                    j -= 1
                if j != -1:
                    return False
                else:
                    return True
            # print(s[i], p[j])
            if len(p[j]) == 1:
                if p[j] == '.' or p[j] == s[i]:
                    return recusive(s, p, i-1, j-1, memo)
                else:
                    return False
            else:
                # iterative all possible 'char*'
                if p[j][0] == '.' or p[j][0] == s[i]:
                    any_true = False
                    if p[j][0] == '.':
                        any_true = recusive(s, p, i, j-1, memo)
                    while i > -1 and not any_true and (s[i] == p[j][0] or p[j][0] == '.'):
                        # print(i-1, '=')
                        any_true = recusive(s, p, i-1, j-1, memo)
                        i -= 1
                    return any_true
                else:  # dont use these 'char*'
                    return recusive(s, p, i, j-1, memo)
        return recusive(s, _p, len(s)-1, len(_p)-1, [])

    def isMatch(self, s, p):
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and \
                        (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]
    
    # O((T+P)^(T+P/2))
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:])  # match empty
            or first_match and self.isMatch(text[1:], pattern)) # or match first char but still keep the pattern
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

    # O(TP)
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        # with '*'
                        # match empty or match first char but still keep the pattern
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        # without '*', just continue
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True # enpty is true
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]


# print(Solution().isMatch("mississippi", "mis*is*p*."))  # False
# print(Solution().isMatch("mississippi", "mis*is*ip*."))  # True
print(Solution().isMatch("aab", "c*a*b"))  # True
# print(Solution().isMatch("ab", ".*"))  # true
# print(Solution().isMatch("aa", "a")) # False
# print(Solution().isMatch("aaa", "aaaa")) # False
# print(Solution().isMatch("baa", ".*a"))  # False
# print(Solution().isMatch("aa", "a*")) # True
# print(Solution().isMatch("aaa", "ab*a*c*a"))  # True
# print(Solution().isMatch("a", ".*..a*"))  # false
# print(Solution().isMatch("", ".*"))  # true
# print(Solution().isMatch("aasdfasdfasdfasdfas",
                        #  "aasdf.*asdf.*asdf.*asdf.*s"))  # true
