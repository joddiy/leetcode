# -*- coding: utf-8 -*-
# file: lengthOfLongestSubstring.py
# author: joddiyzhang@gmail.com
# time: 2018/11/20 2:32 PM
# ------------------------------------------------------------------------


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        max_length = 1
        window_list = [s[0]]
        window_map = {s[0]: 1}
        for i in range(1, len(s)):
            if s[i] in window_map:
                while True:
                    get_v = window_list[0]
                    del window_map[window_list[0]]
                    window_list = window_list[1:]
                    if get_v == s[i]:
                        break
            window_list.append(s[i])
            window_map[s[i]] = 1
            max_length = max(max_length, len(window_list))
        return max_length

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 0
        max_length = 0
        window_map = {}
        while j < len(s):
            if s[j] in window_map:
                # very important, because we don't remove useless values when we move i
                i = max(window_map[s[j]], i)
            max_length = max(max_length, j - i + 1)
            window_map[s[j]] = j + 1
            j += 1
        return max_length


print(Solution().lengthOfLongestSubstring("abba"))
