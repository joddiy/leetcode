from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        for i in range(len(p)-1, len(s)):
            sCounter[s[i]] += 1
            if sCounter == pCounter:
                res.append(i-len(p)+1)
            sCounter[s[i-len(p)+1]] -= 1
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]
        return res

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


print(Solution().findAnagrams("cbaebabacd", "abc"))
