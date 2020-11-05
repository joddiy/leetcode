from tools import *


@print_
def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    ret = []

    def recursive(l, ll, s):
        if l == 0 and ll == 0:
            ret.append(s)
            return
        if l > 0:
            recursive(l - 1, ll + 1, s + "(")
        if ll > 0:
            recursive(l, ll - 1, s + ")")

    recursive(n, 0, "")
    return ret


generateParenthesis(3)
generateParenthesis(1)

