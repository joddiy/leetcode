import collections
import sys


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = collections.defaultdict(int)
        for c in t:
            m[c] += 1
        j = 0

        # identify how many remaining chars in T we still need to find
        count = len(t)
        minLen = sys.maxsize
        minStart = 0
        for i in range(len(s)):
            # only when m[s[i]] > 0, means remaining chars in t
            if m[s[i]] > 0:
                count -= 1
            m[s[i]] -= 1
            # no more chars in T, we start to move j
            while count == 0:
                if (i - j + 1) < minLen:
                    minLen = i-j+1
                    minStart = j
                m[s[j]] += 1
                # only when m[s[i]] > 0, means not chars in S, instad in T again.
                if m[s[j]] > 0:
                    count += 1
                j += 1

        if minLen < sys.maxsize:
            return s[minStart:minStart+minLen]
        return ""


# print(Solution().minWindow('ADOBECODEBANC', 'ABC'))
# print(Solution().minWindow('a', 'a'))
# print(Solution().minWindow('bba', 'ab'))
print(Solution().minWindow('eeaaaaaaaaaaaabbbbbcddee', 'abcdd'))
