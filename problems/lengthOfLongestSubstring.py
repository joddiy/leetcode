from tools import *


class Solution(object):
    # slide window
    @print_
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_ = i = 0
        map_ = {}
        for idx, c in enumerate(s):
            if c in map_:
                # can only find key which is larger than i
                # for example: "abba"
                # first we update i from the first 'b'
                # then we update i from the first 'a'
                # so we should restrict the i
                i = max(i, map_[c])
            # once repeat, start from the next one
            map_[c] = idx + 1 
            max_ = max(max_, idx - i + 1)
        return max_

solution = Solution().lengthOfLongestSubstring

solution("abcabcbb")
solution("bbbbb")
solution("pwwkew")
solution("s")
solution("")
solution("au")
solution("abba")