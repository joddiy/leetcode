from tools import *
import collections


class Solution(object):
    @print_
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret = []
        p_counter = collections.Counter(p)
        s_counter = collections.Counter(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            s_counter[s[i]] += 1
            pre_i = i - len(p) + 1
            if s_counter == p_counter:
                ret.append(pre_i)
            s_counter[s[pre_i]] -= 1
            if s_counter[s[pre_i]] == 0:
                del s_counter[s[pre_i]]
        return ret

    @print_
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        l = len(p)
        p_frequency = [0] * 26
        ss_frequency = [0] * 26
        res = []
        for c in p:
            p_frequency[ord(c) - 97] += 1
        for c in s[0:l]:
            ss_frequency[ord(c) - 97] += 1
        if p_frequency == ss_frequency:
            res.append(0)

        for i in range(1, len(s) - l + 1):
            ss_frequency[ord(s[i - 1]) - 97] -= 1
            ss_frequency[ord(s[i + l - 1]) - 97] += 1
            if p_frequency == ss_frequency:
                res.append(i)

        return res


solution = Solution().findAnagrams

solution("cbaebabacd", "abc")