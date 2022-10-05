from tools import *

phone = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


# O(3^N * 4^M)
@print_
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []

    ret = []
    n = len(digits)

    def recursive(i, s):
        if i >= n:
            ret.append(s)
            return
        for c in phone[digits[i]]:
            recursive(i + 1, s + c)

    recursive(0, "")
    return ret


letterCombinations("23")
letterCombinations("")