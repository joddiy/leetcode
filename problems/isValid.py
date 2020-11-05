from tools import *


@print_
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    left = set("({[")
    for c in s:
        if c in left:
            stack.append(c)
        else:
            if not stack:
                return False
            cc = stack.pop(-1)
            if cc == "(" and c != ")":
                return False
            elif cc == "[" and c != "]":
                return False
            elif cc == "{" and c != "}":
                return False
    return not stack


isValid(r"()[]{}")