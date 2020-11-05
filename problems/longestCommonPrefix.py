from tools import *


# Horizontal scanning
@print_
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    prefix = strs[0]
    for _, s in enumerate(strs, 1):
        i = 0
        while i < min(len(prefix), len(s)) and prefix[i] == s[i]:
            i += 1
        prefix = prefix[:i]
    return prefix


# Vertical scanning
@print_
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    prefix = ""
    for i in range(len(strs[0])):
        cur_c = strs[0][i]
        for _, s in enumerate(strs, 1):
            if i >= len(s) or cur_c != s[i]:
                return prefix
        prefix += cur_c
    return prefix


# Divide and conquer
@print_
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""

    def recursive(i, j):
        if i == j:
            return strs[i]
        m = (j-i+1)//2
        left_ = recursive(i, i+m-1)
        right_ = recursive(i+m, j)
        k = 0
        while k < min(len(left_), len(right_)) and left_[k] == right_[k]:
            k += 1
        return left_[:k]

    return recursive(0, len(strs)-1)


longestCommonPrefix(["flower", "flow", "flight"])
longestCommonPrefix(["dog", "racecar", "car"])
longestCommonPrefix(["d", "d", "d"])
longestCommonPrefix(["", "", ""])
longestCommonPrefix([""])
longestCommonPrefix(["ab", 'a'])