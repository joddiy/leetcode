import math
import pprint
import sys

from tools import *
from collections import defaultdict, Counter

import heapq


class Solution(object):
    @print_
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        len_w = len(words[0])
        len_con = len_w * len(words)
        cnt_con = Counter(words)
        ret = []

        for i in range(len_w):
            cur_cnt = Counter({k: 0 for k in words})
            for j in range(i, len(s) - len_w + 1, len_w):
                word = s[j: j + len_w]
                if word in cur_cnt:
                    cur_cnt[word] += 1
                if j >= len_con + i:
                    r_word = s[j - len_con:j - len_con + len_w]
                    if r_word in cur_cnt:
                        cur_cnt[r_word] -= 1
                if cur_cnt == cnt_con:
                    ret.append(j + len_w - len_con)
        return ret


solution = Solution().findSubstring

# solution(s="barfoothefoobarman", words=["foo", "bar"])
# solution(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"])
solution(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"])
