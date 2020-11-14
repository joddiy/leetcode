from tools import *
from collections import Counter


class Solution(object):
    # O(n^2) Divide And Conquer
    @print_
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def recursive(i, j):
            if i > j:
                return 0
            count = Counter(s[i:j + 1])
            for m in range(i, j + 1):
                if count[s[m]] >= k:
                    continue
                # little optimize
                # skip all invalid char
                n = m + 1
                while n <= j and count[s[n]] < k:
                    n += 1
                return max(recursive(i, m - 1), recursive(n, j))
            return j - i + 1

        return recursive(0, len(s) - 1)

    # O(26 * n) Sliding Window for 26 times
    @print_
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_unique = len(set(s))
        ret = 0
        for cur_unique in range(0, max_unique + 1):
            i, j, unique, count_k = 0, 0, 0, 0
            count_map = Counter()
            # expand
            for j in range(len(s)):
                if count_map[s[j]] == 0:
                    unique += 1
                count_map.update(s[j])
                if count_map[s[j]] == k:
                    count_k += 1
                # shrink
                while unique > cur_unique:
                    if count_map[s[i]] == k:
                        count_k -= 1
                    count_map.subtract(s[i])
                    if count_map[s[i]] == 0:
                        unique -= 1
                    i += 1
                if unique == cur_unique == count_k:
                    ret = max(ret, j - i + 1)
        return ret

solution = Solution().longestSubstring

# solution("ababbc", 2)
solution("cababbd", 2)