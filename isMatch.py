class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n, m = 0, 0
        while n <= len(s) - 1 and m <= len(p) - 1:
            print(n, m)
            print(s[n], p[m])
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
        print(n, m)
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


# print(Solution().isMatch("mississippi", "mis*is*p*.") == False)
# print(Solution().isMatch("mississippi", "mis*is*ip*.") == True)
# print(Solution().isMatch("aab", "c*a*b") == True)
# print(Solution().isMatch("ab", ".*") == True)
# print(Solution().isMatch("aa", "a") == False)
# print(Solution().isMatch("aaa", "aaaa") == False)
# print(Solution().isMatch("baa", ".*a"))
# print(Solution().isMatch("aa", "a*") == True)
print(Solution().isMatch("aaa", "ab*a*c*a") == True)
