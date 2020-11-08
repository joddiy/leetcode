from tools import *


@print_
def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0
    n = len(needle)
    next_ = [0] * n
    next_[0] = -1
    k, j = -1, 0
    while j < n - 1:
        if k == -1 and needle[j] == needle[k]:
            k += 1
            j += 1
            next_[j] = k
        else:
            k = next_[k]
    return next_


strStr("BBC ABCDAB ABCDABCDABDE", "ABCDABD")
# strStr("hello", "ll")
# strStr("aaaaa", "bba")
# strStr("", "")
# strStr("mississippi", "issip")
# strStr("mississippi", "issipi")
# strStr("aabaaabaaac", "aabaaac")