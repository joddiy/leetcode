def solution(word1, word2):
    memo = {}
    n, m = len(word1), len(word2)
    if m < n:
        word1, word2, m, n = word2, word1, n, m

    def recursive(i, j):
        if (i, j) not in memo:
            if i == n:
                ans = m - j
            elif j == m:
                ans = n - i
            else:
                if word1[i] == word2[j]:
                    ans = recursive(i + 1, j + 1)
                else:
                    # insert, delete, replace
                    ans = min(recursive(i, j + 1), recursive(i + 1, j),
                              recursive(i + 1, j + 1)) + 1
            memo[i, j] = ans
        return memo[i, j]

    return recursive(0, 0)


print(solution("horse", "ros"))