from tools import *


@print_
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    ret = ""
    j = 0
    while True:
        cur_c = ""
        for i in range(len(strs)):
            s = strs[i]
            if j >= len(s):
                return ret
            c = s[j]
            if not cur_c:
                cur_c = c
            elif c != cur_c:
                return ret
        j += 1
        ret += cur_c


longestCommonPrefix(["flower", "flow", "flight"])
longestCommonPrefix(["dog", "racecar", "car"])
longestCommonPrefix(["d", "d", "d"])
longestCommonPrefix(["", "", ""])
longestCommonPrefix([""])
