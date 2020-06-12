phone = {'2': ['a', 'b', 'c'],
         '3': ['d', 'e', 'f'],
         '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'],
         '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'],
         '8': ['t', 'u', 'v'],
         '9': ['w', 'x', 'y', 'z']}

# O(3^N * 4^M)
def solution(digits):
    ret = []
    if not digits:
        return ret

    def recursion(prefix, digits):
        if not digits:
            ret.append(prefix)
        else:
            for c in phone[digits[0]]:
                recursion(prefix+c, digits[1:])
    recursion("", digits)
    return ret


print(solution("23"))
print(solution(""))