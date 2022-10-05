from tools import *


@print_
def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    s = s.strip()
    if not s:
        return 0
    f_c = ord(s[0])
    negative = False
    if f_c == 45:
        negative = True
        s = s[1:]
    if f_c == 43:
        s = s[1:]
    s = (ord(c) for c in s)
    ret = 0
    for c in s:
        if c < 48 or c > 57:
            break
        ret = ret * 10 + c - 48
    if ret > 0x7FFFFFFF:
        return -2**31 if negative else 2**31 - 1
    return -ret if negative else ret


myAtoi("")
myAtoi("+1")
myAtoi("42")
myAtoi("   -42")
myAtoi("4193 with words")
myAtoi("words and 987")
myAtoi("-91283472332")