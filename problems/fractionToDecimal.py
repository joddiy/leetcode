from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not numerator:
            return "0"

        negative = (numerator > 0) ^ (denominator > 0)

        numerator = abs(numerator)
        denominator = abs(denominator)

        ret = ""
        while numerator > denominator:
            ret += str(numerator // denominator)
            numerator = numerator % denominator
        if not ret:
            ret = "0"

        n_s = defaultdict(int)
        decimal = []
        idx = 0
        while numerator != 0 and numerator not in n_s:
            n_s[numerator] = idx
            numerator *= 10
            decimal.append(str(numerator // denominator))
            numerator = numerator % denominator
            idx += 1

        if numerator:
            decimal.insert(n_s[numerator], "(")
            decimal.append(")")

        if decimal:
            ret += "." + "".join(decimal)

        if negative:
            ret = "-" + ret

        return ret


solution = Solution().fractionToDecimal

solution(0, -5)
solution(1, 6)
# solution(1, 2)
# solution(2, 1)
# solution(2, 3)
# solution(4, 333)
# solution(1, 5)
solution(-50, 8)