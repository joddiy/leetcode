import sys
from tools import *


@print_
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    negative = (x < 0)
    x = abs(x)
    y = 0
    while x > 0:
        res = x % 10
        x = x // 10
        y = y * 10 + res
    y = -y if negative else y
    return 0 if abs(y) > 0x7FFFFFFF else y


reverse(123)
reverse(-123)
reverse(120)
reverse(0)