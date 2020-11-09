from tools import *
from collections import Counter
import sys


class Solution(object):
    @print_
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(s)
        count = len(t)
        count_w = Counter(t)
        b, l = 0, sys.maxsize  # begin, length
        i, j = 0, 0  # slide window
        while j < n:
            # only minus count for the word in t
            if count_w[s[j]] > 0:
                count -= 1
            count_w[s[j]] -= 1

            # once count == 0
            while not count:
                # update b and l
                if (j - i + 1) < l:
                    l = (j - i + 1)
                    b = i

                count_w[s[i]] += 1
                # only restore the count for
                # the word in t
                if count_w[s[i]] > 0:
                    count += 1
                i += 1

            j += 1

        if l < sys.maxsize:
            return s[b:b + l]
        return ""


solution = Solution().minWindow

# solution("ADOBECODEBANC", "ABC")
solution("ABC", "ABC")