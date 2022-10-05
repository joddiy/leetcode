from tools import *


@print_
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    map_ = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s_ = (s[i] for i in range(len(s) - 1, -1, -1))
    ret = 0
    l_c = -1
    for c in s_:
        c = map_[c]
        if c >= l_c:
            ret += c
            l_c = c
        else:
            ret -= c
    return ret


romanToInt("III")
romanToInt("IV")
romanToInt("IX")
romanToInt("LVIII")
romanToInt("")