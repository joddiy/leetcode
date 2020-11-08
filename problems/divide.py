from tools import *


@print_
def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    positive = (dividend < 0) is (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        tmp, i = divisor, 1
        while dividend >= tmp:
            dividend -= tmp
            res += i
            i <<= 1
            tmp <<= 1

    if res > 0x7FFFFFFF:
        return 2**31 - 1 if positive else -2**31

    return res if positive else -res

divide(10, 3)
divide(20, 3)