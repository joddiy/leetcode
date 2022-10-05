from tools import *


class Solution(object):
    @print_
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        n = len(needle)
        m = len(haystack)
        next_ = [0] * n

        def get_next():
            next_[0] = -1
            # k is the prefix
            # j is the suffix
            k, j = -1, 0
            while j < n - 1:
                # p[k] == p[j]
                # next[j + 1] = next[j] + 1 = k + 1
                if k == -1 or needle[j] == needle[k]:
                    k += 1
                    j += 1
                    # for example "abab"
                    # when we check the last 'b'
                    # its same prefix and suffix is "a"
                    # however, beacuse the 'b' after prefix 'a'
                    # is same to the 'b' after suffix, which means
                    # mismatch. So we can see, once it mismatch the second
                    # 'b', it must mismatch the first 'b'
                    # so we don't need check from the first 'b'
                    # we can check it's next_[1] then
                    if needle[j] != needle[k]:
                        next_[j] = k
                    else:
                        next_[j] = next_[k]
                # current k cannot let prefix == suffix
                # need to try a shorter prefix ans suffix
                # the prefix and suffix need to be valid
                # for example "DAB"
                # we need to check "DA" and "AB"
                # in another word, we actually are finding 
                # a longer prefix == suffix in its prefix
                # os its prefix is j=k, and its valid prefix
                # is next_[k]
                else:
                    k = next_[k]

        def kmp():
            i, j = 0, 0
            while i < m and j < n:
                if j == -1 or haystack[i] == needle[j]:
                    i += 1
                    j += 1
                else:
                    j = next_[j]

            if j == n:
                return i - j
            else:
                return -1

        get_next()

        return kmp()


solution = Solution().strStr

solution("BBC ABCDAB ABCDABCDABDE", "ABCDABD")
solution("hello", "ll")
solution("aaaaa", "bba")
# solution("", "")
# solution("mississippi", "issip")
# solution("mississippi", "issipi")
# solution("aabaaabaaac", "aabaaac")