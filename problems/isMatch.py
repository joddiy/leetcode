def solution(s, p):
    memo = {}
    m, n = len(s), len(p)

    def recursive(i, j):
        if (i, j) not in memo:
            if j == n:
                ans = i == m
            else:
                first_match = i < m and p[j] in (s[i], '.')
                if j + 1 < n and p[j + 1] == '*':
                    ans = recursive(
                        i, j + 2) or first_match and recursive(i + 1, j)
                else:
                    ans = first_match and recursive(i + 1, j + 1)
            memo[i, j] = ans
        return memo[i, j]

    return recursive(0, 0)


print(solution("aa", "a"))
print(solution("aa", "a*"))
print(solution("ab", ".*"))
# print(solution("aab", "c*a*b"))
# print(solution("mississippi", "mis*is*p*."))
