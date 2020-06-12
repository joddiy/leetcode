from collections import Counter
import sys


def solution(s, t):
    n = len(s)
    i, j = 0, 0
    c_t = Counter(t)
    count = len(t)
    b, l = 0, sys.maxsize
    while j < n:
        if c_t[s[j]] > 0:
            count -= 1
        c_t[s[j]] -= 1

        while not count:
            if (j - i + 1) < l:
                l = j - i + 1
                b = i
            c_t[s[i]] += 1
            if c_t[s[i]] > 0:
                count += 1
            i += 1
        j += 1
    if l < sys.maxsize:
        return s[b:b + l]
    return ""


print(solution("ADOBECODEBANC", "ABC"))
