import collections
import sys


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = collections.defaultdict(int)  # count the chars in t
        for c in t:
            m[c] += 1
        print(m)

        j = 0

        count = len(t)
        minLen = sys.maxsize
        minStart = 0

        for i in range(len(s)):
            if m[s[i]] > 0:
                count -= 1

            m[s[i]] -= 1
            print(m,count)

            # if count = 0, we start to constract the left point
            while count == 0:
                if (i - j + 1) < minLen:
                    minLen = i-j+1
                    # DONT FORGET THE MIN START IF YOU NEED TO RETURN THE STRING
                    minStart = j
                m[s[j]] += 1
                # DONT FORGET TO CHECK THE > 0
                # once the count is changed, break the loop and find next
                # right point
                # for the char not in the t,
                # the value cannot be large than 0
                # so it won't influence the count
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
