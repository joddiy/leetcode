# O(n^2)
def solution(s):
    n = len(s)
    dp = [[0] * n for i in range(n + 1)]
    ret = ""
    max_len = 0
    # i is the length, j is the start position
    for i in range(1, len(s) + 1):
        for j in range(len(s) - i + 1):
            # case 1, single char
            if i == 1:
                dp[i][j] = 1
            # case 2, continuous smae char
            elif i == 2:
                if s[j] == s[j + 1]:
                    dp[i][j] = 2
            else:
                if dp[i - 2][j + 1] > 0 and s[j] == s[j + i - 1]:
                    dp[i][j] = dp[i - 2][j + 1] + 2
            if dp[i][j] > max_len:
                max_len = dp[i][j]
                ret = s[j:j + i]
    return ret


# print(solution("babad"))
print(solution("abcda"))
