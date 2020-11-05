def solution(s):
    n = len(s)
    if n <= 1:
        return n
    dp = [[0] * (n + 1) for _ in range(n)]  # (start_pos, len)
    ret = 0
    for i in range(1, n + 1):
        for j in range(0, n - i + 1):
            if i == 1 or (i == 2 and
                          s[j] == s[j + 1]) or (s[j] == s[j + i - 1] and
                                                dp[j + 1][i - 2]):
                dp[j][i] = 1
                ret += 1
    return ret


# print(solution("a"))
# print(solution(""))
# print(solution("abc"))
print(solution("aaa"))